from trainingBot import *
import Globals



def basic_elvesless_defence(game):
    """
    this function is responsble for the portal to summon_ice_troll when needed
    
    :param: game
    :return: nothing
    :type void
    
    """
    
    for portal in game.get_my_portals() :
        
        if are_elves_coming(game, portal):
            print "summon_ice_troll because elves are coming!!"
            if not summon(game,portal, ICE):
                mana_state = "save mana"
    
    
    sort_portal_by_best_to_defend(game)
    print "enemy attack force: %s" % enemy_attacking_units_total_health(game)
    print "our defence force %s"% current_defence_total_health(game)
    print "%s portals should summon_ice_troll because of enemy attack force" %how_many_portals_should_defend_by_game_status(game)
    for i in range(0, how_many_portals_should_defend_by_game_status(game), 1):
        if len(game.get_my_portals()) > i:
            summon(game,game.get_my_portals()[i], ICE)
    
    if len(dangerous_elves(game)) >= len(game.get_all_enemy_elves()) - 1:
        spam_ice_troll(game)

def spam_ice_troll(game):
    
    """
    this function says to the defence to spawn us many ice_trolls that he can
    
    :param: game
    :type: void
    """
    
    print "spaming ice_trolls!!"
    if len(game.get_my_ice_trolls()) < len(game.get_enemy_lava_giants()):
        if game.get_my_portals():
            for portal in game.get_my_portals():
                if portal.distance(game.get_my_castle()) < portal.distance(game.get_enemy_castle()):
                    summon(game, portal , ICE)
    
    
    
    
def is_suicide_for_win_better_then_defend(game):
    
    # need rework!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    """
    This function is very importent!!!
    
    when a enemy rushes us it should calculate weather or not
    we can defet them before us
    
    factors should be considerd:
    *turns to arrive (considerd in distance and building in the way)
    *mana_state to summon_lava_giant 
    *castles_health
    
    
    :param: game
    :return True if we can win, False if not
    :type: bool
    
    """
    my_castle = game.get_my_castle()
    enemy_castle = game.get_enemy_castle()
    enemy_most_dangrous_elf = get_closest_enemy_elf(game, my_castle)
    my_most_dangrous_elf = get_closest_my_elf(game, enenemy_castle)
    
    if enemy_most_dangrous_elf.distance(my_castle) > my_most_dangrous_elf.distance(enemy_castle) and mmy_most_dangrous_elf.current_health > game.elf_max_health > 3 :
        if len(game.get_my_mana_fountains()) > len(game.get_enemy_mana_fountains()) or game.get_my_mana() > game.get_enemy_mana():
            return True
    if count_obstacles_in_my_elf_way_to_castle(game, my_most_dangrous_elf) < count_obstacles_in_enemy_elf_way_to_castle(game, enemy_most_dangrous_elf) and \
        enemy_most_dangrous_elf.distance(my_castle) - my_most_dangrous_elf.distance(enemy_castle) < count_obstacles_in_my_elf_way_to_castle(game, my_most_dangrous_elf) * game.elf_max_speed / game.speed_up_multiplier:
        if len(game.get_my_mana_fountains()) > len(game.get_enemy_mana_fountains()) or game.get_my_mana() > game.get_enemy_mana():
                return True
    if enemy_most_dangrous_elf.distance(my_castle) > my_most_dangrous_elf.distance(enemy_castle) and mmy_most_dangrous_elf.current_health > game.elf_max_health > 3:
        if count_obstacles_in_my_elf_way_to_castle(game, my_most_dangrous_elf) < count_obstacles_in_enemy_elf_way_to_castle(game, enemy_most_dangrous_elf) and \
            enemy_most_dangrous_elf.distance(my_castle) - my_most_dangrous_elf.distance(enemy_castle) < count_obstacles_in_my_elf_way_to_castle(game, my_most_dangrous_elf) * game.elf_max_speed / game.speed_up_multiplier:
            return True
    
    return False


def count_obstacles_in_my_elf_way_to_castle(game, elf):
    
    """
    this function returns the nummber of buldings between attacking elf to enemy castle
    *factor in suiciding 
    
    :param game, elf(attacking_elf)
    :return num of buildings in the way
    :type: int
    
    """
    count = 0
    for portal in game.get_enemy_portals():
        if portal.distance(elf) + portal.distance(game.get_enemy_castle())  < elf.distance(game.get_enemy_castle()) + game.portal_size or \
            portal.distance(elf) + portal.distance(game.get_enemy_castle())  > elf.distance(game.get_enemy_castle()) - game.portal_size:
            
            count += 2 # portals are harder to kill so i consider them as 2 (in comperisson it wont matter)
    
    for mana_fountain in game.get_enemy_mana_fountains():
        if mana_fountain.distance(elf) + mana_fountain.distance(game.get_enemy_castle())  < elf.distance(game.get_enemy_castle()) + game.portal_size or \
            mana_fountain.distance(elf) + mana_fountain.distance(game.get_enemy_castle())  > elf.distance(game.get_enemy_castle()) - game.portal_size:
            
            count +=1

    return count

def count_obstacles_in_enemy_elf_way_to_castle(game, elf):
    
    """
        this function returns the nummber of buldings between attacking enemy_elf to my castle
    *factor in suiciding 
    
    :param game, elf(attacking_elf)
    :return num of buildings in the way
    :type: int
    
    
    """
    count = 0
    for portal in game.get_my_portals():
        if portal.distance(elf) + portal.distance(game.get_my_castle())  < elf.distance(game.get_my_castle()) + game.portal_size or \
            portal.distance(elf) + portal.distance(game.get_my_castle())  > elf.distance(game.get_my_castle()) - game.portal_size:
            
            count += 2 # portals are harder to kill so i consider them as 2 (in comperisson it wont matter)
    
    for mana_fountain in game.get_my_mana_fountains():
        if mana_fountain.distance(elf) + mana_fountain.distance(game.get_my_castle())  < elf.distance(game.get_my_castle()) + game.portal_size or \
            mana_fountain.distance(elf) + mana_fountain.distance(game.get_my_castle())  > elf.distance(game.get_my_castle()) - game.portal_size:
            
            count +=1
            
    return count
    
def dangerous_elves(game):
    
    """
    this function return a list of the dangerous_elves, close to our castle
    
    param: game
    type: list[elves]
    
    """
    dangerous_elves = []
    
    for enemy_elf in game.get_enemy_living_elves():
        if enemy_elf.distance(game.get_my_castle()) < enemy_elf.distance(game.get_enemy_castle()) and not is_targeted_by_my_icetroll(game, enemy_elf):
            dangerous_elves.append(enemy_elf)
    return dangerous_elves
        

    
def how_many_portals_should_defend_by_game_status(game):
    """
    
    this function checks how many portals should summon_ice_troll 
    based on the current game status (enemy_creatures and my_creatures)
    
    :param: game
    :returns the health of our defence
    :type: int 
    
    """
    if not game.get_my_portals():
        return 0
    
    
    doesnt_worth_summon_ice_troll_attack_power = 5
    count_defensive_portal = 0
    
    
    if enemy_attacking_units_total_health(game) - current_defence_total_health(game) <= doesnt_worth_summon_ice_troll_attack_power:
        return 0
    
    else :
        if enemy_attacking_units_total_health(game) > current_defence_total_health(game) + 10:
            if enemy_attacking_units_total_health(game) > current_defence_total_health(game) +  game.ice_troll_max_health :
                for portal in game.get_my_portals():
                    if portal.distance(game.get_my_castle()) > portal.distance(game.get_enemy_castle()) :
                        count_defensive_portal += 1
                return count_defensive_portal
            if len(game.get_my_portals()) > 1:
                return 2
    return 1
    
    


    
def enemy_attacking_units_total_health(game):
    """
    this function
    
    :param: game
    :returns: the enemy attacking units total health 
    :type:int
    
    """
    
    total_enemy_attacking_units_health = 0
    if game.get_enemy_lava_giants():
        for enemy_lava_giant in get_dangerous_enemy_lava_giant(game):
            if enemy_lava_giant.distance(game.get_my_castle()) < enemy_lava_giant.distance(game.get_enemy_castle()):
                total_enemy_attacking_units_health += enemy_lava_giant.current_health
    if game.get_enemy_living_elves():
        for enemy_elf in game.get_enemy_living_elves():
            if enemy_elf.distance(game.get_my_castle()) < enemy_elf.distance(game.get_enemy_castle()):
                total_enemy_attacking_units_health += enemy_elf.current_health
    if game.get_enemy_ice_trolls():
        for enemy_ice_troll in game.get_enemy_ice_trolls():
            if enemy_ice_troll.distance(game.get_my_castle()) < enemy_ice_troll.distance(game.get_enemy_castle()):
                total_enemy_attacking_units_health += enemy_ice_troll.current_health
    if game.get_enemy_portals():
        for enemy_portal in game.get_enemy_portals():
            if enemy_portal.distance(game.get_my_castle()) < enemy_portal.distance(game.get_enemy_castle()) and enemy_portal.is_summoning:
                total_enemy_attacking_units_health += game.lava_giant_max_health
                
    return total_enemy_attacking_units_health



def current_defence_total_health(game):
    
    """
    
    the power of the the defence is calculated by 
    the difrence between enemy combined attacking unit health
    and our defence units health 
    
    
    :param: game
    :returns the health of our defence units
    :type: int
    
    """
    
    total_my_defensive_units_health = 0
    if game.get_my_ice_trolls():
        for my_ice_troll in game.get_my_ice_trolls():
            if my_ice_troll.distance(game.get_my_castle()) < my_ice_troll.distance(game.get_enemy_castle()):
                total_my_defensive_units_health += my_ice_troll.current_health
    if game.get_my_living_elves():
        for my_elf in game.get_my_living_elves():
            if  my_elf.distance(game.get_my_castle()) < my_elf.distance(game.get_enemy_castle()):
                total_my_defensive_units_health += my_elf.current_health
    if game.get_enemy_ice_trolls() and game.get_my_lava_giants():
        for my_lava_giant in game.get_my_lava_giants():
            for enemy_ice_troll in is_targeted_by_enemy_icetroll(game, my_lava_giant):
                if enemy_ice_troll.distance(game.get_my_castle()) < enemy_ice_troll.distance(game.get_enemy_castle()):
                    total_my_defensive_units_health += enemy_ice_troll.current_health # in compare make them not matter
    if game.get_my_portals():
        for my_portals in game.get_my_portals():
            if my_portals.distance(game.get_my_castle()) < my_portals.distance(game.get_enemy_castle()) and my_portals.currently_summoning == "IceTroll":
                total_my_defensive_units_health += game.ice_troll_max_health
         
    return total_my_defensive_units_health
         

def sort_portal_by_best_to_defend(game):
    
    #not finished
    
    """
    sorts our portals by best to defence
    
    :param game
    :returns
    :type: void
    
    """
    
    # the factor is min(portal.distance(closest_enemy_lava_giant_to_my_castle) + portal.distance(closest_enemy_lava_giant_to_my_castle))
    # if 2 portals has the same value the need to check if the closer to the enemy can spawn in time to be effective
    
    
    
    
def are_elves_coming(game, portal):
    """
    
    This function checks weather or not elves coming to given portal
    
    
    :param: game, portal
    :returns: if elves coming - True, else False
    :type: bool
    
    """
    prev_game = Globals.prev_game
    
    for enemy_elf in game.get_enemy_living_elves():
            
            
            curr_enemy_elf_distance = enemy_elf.distance(portal)
            prev_enemy_elf = get_by_unique_id(prev_game, enemy_elf.unique_id)
            if prev_enemy_elf:
                prev_enemy_elf_distance = prev_enemy_elf.distance(portal)
                if prev_enemy_elf_distance > curr_enemy_elf_distance:  # if the enemy elf is running away from portal
                    continue
                
            attacking_pos = portal.get_location().towards(enemy_elf, game.portal_size + game.elf_attack_range)
            if turns_to_travel(game, enemy_elf, attacking_pos) < game.ice_troll_summoning_duration + 1 and not is_targeted_by_my_icetroll(game, enemy_elf):
                return True
                print "summon ice, close elf"
            
            

def build_bunker_fast(game, elves_not_acted):
    """
    this function is responsble to build our base, usally called
    after killed enemy elves and wont reach end game in time 
    
    :param: game
    :param: list[elves_not_acted]
    :type: void
    
    """
         
    for elf in elves_not_acted:
        if abs(elf.distance(game.get_my_castle()) - elf.distance(game.get_enemy_castle())) < game.get_my_castle().distance(game.get_enemy_castle()) / 4:
            if not build(game, elf, PORTAL):
                rush_to_loc(game, elf, closest_possible_building_location(game, elf))
        else:
            if not build(game, elf, MANA_FOUNTAIN):
                rush_to_loc(game, elf, closest_possible_building_location(game, elf))
  
    
def closest_possible_building_location(game, elves_not_acted):
    
    """
    
    
    """
    
    for elf in elves_not_acted:
        for y in range(0,game.rows, 5): # I check every 5th point to shorten the time run
            possible_location = location(elf.get_location().col, y)
            if game.can_build_portal_at(possible_location) and elf.distance(possible_location) < elf.distance(closest_possible_location):
                closest_possible_location = possible_location
            
        for r in range(game.portal_size, elf.distance(closest_possible_location), 5):
            for location in get_circle(game, elf, r):
                if game.can_build_portal_at(location):
                    return location
        
        return closest_possible_location





def build_smart_bunker(game, elves_not_acted):
    
    """
    
    """
    for elf in elves_not_acted:
        max_num_of_mana_fountain_needed = 5
        if len(game.get_my_mana_fountains()) <= max_num_of_mana_fountain_needed:
            build(game, elf, MANA_FOUNTAIN)
        else:
            closest_possible_location = location()
            for possible_location in smart_portal_locations(game):
                if possible_location < closest_possible_location:
                    closest_possible_location = possible_location
                    
            if elf.get_location() == closest_possible_location:
                build(game, elf, PORTAL) 
            else: 
                if elf.distance(closest_possible_location) >= (game.speed_up_expiration_turns - 1) * game.elf_max_speed:
                    rush(game, elf, closest_possible_location)
                else:
                    smart_movment(game, elf, closest_possible_location)
   
'''             
def smart_defencive_portal_locations(game)
    
    """
    
    """
    smart_locations = []
    enemy_portals_we_dont_counter
    
    
    for r in range(game.castle_size + game.portal_size, game.get_my_castle.distance(game.get_enemy_castle)/2, 10):# 10 to run fewer times
        for
'''
    
    
    
def destroy_enemy_buildings(game, elves_not_acted): 
    
    """
    
    """
    print "destroying buildings"
    
    for elf in elves_not_acted:
        if game.get_enemy_portals():
            attack_closest_enemy_portal(game, elf)
            elves_not_acted.remove(elf)
        elif game.get_enemy_mana_fountains():
            attack_closest_enemy_mana_fountain(game, elf)
            elves_not_acted.remove(elf)
        
    return elves_not_acted 
             
        
def counter_rush(game, elves_not_acted):
    
    """
    this function responsble to hunt the enemy elves when coming in rush
    
    :param: game
    :type: void
    
    """
    
    enemy_rushing_elf = get_closest_enemy_elf(game, game.get_my_castle())
    future_enemy_rushing_elf_loaction = enemy_rushing_elf.get_location.towards(game.get_my_castle() , enemy_rushing_elf.distance(game.get_my_castle()) / 2)
    if does_win_fight(game, elf, enemy_rushing_elf):
        if turns_to_travel(game, elf, enemy_rushing_elf.get_location) < 5:
            hunt_enemy_elves_with_speed(game, elf, enemy_rushing_elf)
        else:
            rush_to_loc(game,elf,future_enemy_rushing_elf_loaction)
    else:
        
        for elf in elves_not_acted:
            if turns_to_travel(game, elf, enemy_rushing_elf.get_location) < 5:
                hunt_enemy_elves_with_speed(game, elf, enemy_rushing_elf)
            else:
                rush_to_loc(game,elf,future_enemy_rushing_elf_loaction)




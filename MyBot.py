from elf_kingdom import *

ICE = "ice"
LAVA = "lava"

def do_turn(game):

    game.get_my_living_elves()[0].location = Location(0,0)
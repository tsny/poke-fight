from pokemon import *
from utils import *
from input import *

import argparse

parser = argparse.ArgumentParser(description='Jump right into a Pokemon fight!')
parser.add_argument('-n', '--num', type=int, help='Choose a pokemon to fight using their number with this arg')

args = parser.parse_args()
num = args.num

player = Pokemon(num)
enemy = Pokemon()

clearScreen()

print("A wild " + enemy.name + " appears!")

if (enemy.isShiny):
    print("Wow! It's shiny!")

print("Go! " + player.name + "!\n")

getInput()


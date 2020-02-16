from pokemon import *
from utils import *
from input import *

args = parseArgs()
num = args.num

clearScreen()

print("Loading Pokemon...")

player = Pokemon(num)
enemy = Pokemon()

print("A wild " + enemy.name + " appears!")

if (enemy.isShiny):
    print("Wow! It's shiny!")

print("Go! " + player.name + "!\n")

while (getInput() == True):
    print("")


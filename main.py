from pokemon import *
from utils import *
from input import *

args = parseArgs()
num = args.num

player = Pokemon(num)
enemy = Pokemon()

clearScreen()

print("A wild " + enemy.name + " appears!")

if (enemy.isShiny):
    print("Wow! It's shiny!")

print("Go! " + player.name + "!\n")

getInput()


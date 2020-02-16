from pokemon import *
from utils import *
from input import *

enemy = Pokemon()
player = Pokemon()

clearScreen()

print("A wild " + enemy.name + " appears!")

if (enemy.isShiny):
    print("Wow! It's shiny!")

print("Go! " + player.name + "!\n")

getInput()


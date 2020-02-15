from pokemon import *

enemy = Pokemon()
player = Pokemon()

print(chr(27) + "[2J")

print("A wild " + enemy.name + " appears!")

if (enemy.isShiny):
    print("Wow! It's shiny!")

print("Go! " + player.name + "!")



#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint(r.json())


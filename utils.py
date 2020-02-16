import random

def chance(range):
    num = random.randrange(range)
    other = random.randrange(range)
    return num == other

def clearScreen():
    print(chr(27) + "[2J")

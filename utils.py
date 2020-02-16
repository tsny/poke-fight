import random
import argparse

def chance(range):
    num = random.randrange(range)
    other = random.randrange(range)
    return num == other

def clearScreen():
    print(chr(27) + "[2J")

def parseArgs():
    parser = argparse.ArgumentParser(description='Jump right into a Pokemon fight!')
    parser.add_argument('-n', '--num', type=int, help='Choose a pokemon to fight using their number with this arg')

    return parser.parse_args()

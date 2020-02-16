import random
import requests
from utils import chance

class Pokemon:
    def __init__(self):
        rand = randPokemon()
        self.name = rand["name"].capitalize() 
        self.isShiny = calculateShiny()
        self.power = random.randrange(50)
        #self.hp = rand["hp"]

def randPokemon():
    num = str(random.randrange(500))
    url = "https://pokeapi.co/api/v2/pokemon/" + num + "/"
    return requests.get(url).json()

def calculateShiny():
    return chance(8000)


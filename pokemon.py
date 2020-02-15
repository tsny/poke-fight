import random
import requests

class Pokemon:
    def __init__(self):
        rand = Random().json()
        self.name = rand["name"].capitalize() 
        self.isShiny = calculateShiny()
        #self.hp = rand["hp"]

def Random():
    num = str(random.randrange(500))
    url = "https://pokeapi.co/api/v2/pokemon/" + num + "/"
    r = requests.get(url)
    return r

def calculateShiny():
    num = random.randrange(8000)
    other = random.randrange(8000)
    return num == other

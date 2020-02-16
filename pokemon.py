import random
import requests
from utils import chance

class Pokemon:
    def __init__(self, num=None):
        if (num is None):
            num = random.randrange(500)
        json = hitApi(num)
        self.name = json["name"].capitalize() 
        self.isShiny = calculateShiny()
        self.power = random.randrange(50)

def calculateShiny():
    return chance(8000)

def hitApi(num):
    num = str(num)
    if (not num.isnumeric):
        print(num + " is not a valid pokemon number") 
        return None
    url = "https://pokeapi.co/api/v2/pokemon/" + num + "/"
    return requests.get(url).json()



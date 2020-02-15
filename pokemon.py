import random
import requests

class Pokemon:
    def __init__(self):
        rand = Random().json()
        self.name = rand["name"].capitalize() 
        #self.hp = rand["hp"]

def Random():
    num = str(random.randrange(500))
    url = "https://pokeapi.co/api/v2/pokemon/" + num + "/"
    r = requests.get(url)
    return r


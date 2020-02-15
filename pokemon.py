import random
import requests

class Pokemon:
    def __init__(self):
        self.name = Random()


def Random():
    num = str(random.randrange(500))
    url = "https://pokeapi.co/api/v2/pokemon/" + num + "/"
    r = requests.get(url)
    return r.json()["name"].capitalize() 


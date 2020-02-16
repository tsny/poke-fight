from utils import * 

def getInput():
    prompt()
    val = input("Enter action: ") 
    while (not val.isnumeric()):
        print("Input invalid!")
        val = input("Enter action: ") 

def prompt():
    print("1. Attack")
    print("2. Items")
    print("3. Swap PKMN")
    print("4. Run\n")

def run():
    succeed = chance(60)
    print("Ran away!" if succeed else "Couldn't run!")

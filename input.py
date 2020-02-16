from utils import * 

class Switcher(object):

    def run(self):
        failedRun = chance(60)
        print("Couldn't Run!" if failedRun else "Ran away!")
        return not failedRun

    def attack(self):
        print("attack")

    def item(self):
        print("item")

    def swapPkmn(self):
        print("Swap")

    def action(self, argument):
        """Dispatch method"""
        actions = {
                1: "attack",
                2: "item",
                3: "swapPkmn",
                4: "run"
            }

        chosen = actions.get(int(argument))
        return getattr(self, chosen, lambda: "invalid option")


def getInput():
    prompt()
    val = input("Enter action: ") 
    while (not val.isnumeric()):
        print("Input invalid!")
        val = input("Enter action: ") 

    action = Switcher().action(val)
    action()
    return True

def prompt():
    print("1. Attack")
    print("2. Items")
    print("3. Swap PKMN")
    print("4. Run\n")

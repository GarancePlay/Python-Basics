
#05 fonctions

"""
    Fonctions deja abordees : 

        print(), input()
        type(), int(), float(), str(), bool()

"""

def say_hello():
    print("Hello!")

def say(name='null', age=0, message="null"):
#On definit des parametres par defaut
    print("{} ({} ans) : {}".format(name,age,message))

say_hello()

say("Garance",22,"Bienvenue au cours d'introduction a Python")

say(message="Yo", name="Caro", age=21)
#On peut renseigner les parametres dans le desordre

say(name="Tom",message="Bonsoir.")
#On peut ne pas renseigner tous les parammetres


"""
"""


def show_inventory(*items):
# * : On peut avoir un nombre infini d'arguments   
    for item in items:
        print(item)

show_inventory("sword")
show_inventory("sword","bow","mana potion")


"""
"""


def max(a,b):
    if a > b :
        return a
    elif b > a:
        return b
    else :
        return "egalite"


print(max(45,12))

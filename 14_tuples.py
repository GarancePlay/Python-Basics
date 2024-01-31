
#14 tuples

"""
    Apres leurs creations, les tuples sont imuables

    tuple = () -> tuple vide
    tuple = (45,) -> une seule valeur
    tuple = (45,67) -> Plusieurs valeurs

    2 raisons d'utiliser les tuples :

        -affectation multiple de variable
        -retour multiple de fonction
"""


#Creation d'un tuple
tuple = (35,64)
print(type(tuple))

print(tuple[0]) #acces comme dans les listes


"""
"""


#Affectation multiple
n1, n2 = (45,64)
print(n1,n2)

n1=128
print(n1)
#seul cas ou on peut modifier la valeur des variables


"""
"""


#Retour multiple de fonction

def get_player_postion():
    posX = 124
    posY = 236

    return (posX, posY) #retourne un tuple

#Programme principal

x = 0
y = 0

print("Player position : ({} / {})".format(x,y))

(x,y) = get_player_postion()

print("Player position : ({} / {})".format(x,y))
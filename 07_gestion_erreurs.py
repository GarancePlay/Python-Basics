
#07 gestion d'erreur

user_age = input("Entrez votre age : ")

try:
    user_age = int(user_age)
except:
    print("Age incorrect")
else:
#Si tout fonctionne
    print("Tu as {} ans".format(user_age))
finally:
#S'execute dans tous les cas
    print("Fin du prgramme")


"""
"""


number1 = 150
number2 = input("Entrez le diviseur : ")

try:
    number2 = int(number2)
    print("result : {}".format(number1 / number2))
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par 0")
except ValueError:
    print("saisie incorrect")


"""
"""


try:
    age = input("Age : ")
    age = int(age)
    assert age > 25
    # leve une AssertionError si la condition n'est pas verifie

except AssertionError:
    print("Exception caught!")


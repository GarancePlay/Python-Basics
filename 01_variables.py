
#01 Variables

age = 22
name = "Garance"
wallet = 12.9
motivation = True

print(type(age))
print(type(name))
print(type(wallet))
print(type(motivation))

"""
"""

print("Age:",age,", Prenom:",name,".\n")

texte = "Age de la personne : {} ans, Nom de la personne : {}."
print(texte.format(age,name))

"""
"""

playerName = input("Entrez un nom de joueur : ") 
#recupere la donnee saisie au clavier par l'utilisateur
#string par defaut

print("Bienvenue ",playerName,"!")

"""
"""

prixHT = input("Entrez prix HT : ")
prixHT = int(prixHT)

prixTTC = prixHT + (prixHT * 20 / 100)
print("Prix TTC : ",prixTTC)

valeurBool = True
valeurBool = int(valeurBool)
print(valeurBool)


#13 Listes

"""
    En python, pas de tableau!
    On peut mettre dans une meme listes des objets differents
"""


#------------------Creation d'une liste------------------#


l = list()
l = [] #liste vide
l = [0,2,4,"Voiture",True]

l = [7] * 12 #contient 12 * l'elt. 7
print(l)

l = range(20) #rempli la liste 0,1,2...19

l = ["Garance","Youssef","Guillaume","Melina","Marie","Pierre"]


#------------------Parcourir une liste------------------#


#option 1
for value in l:
    print(value)

#option 2
i = 0
while i < len(l):
    print(l[i])
    i += 1


#------------------Affichage cible d'une liste------------------#
    

print(l[:]) #afficher la totalite de la liste
print(l[:2]) #afficher les deux permiers elts. de la liste
print(l[-2:]) #afficher les deux derniers elts. de la liste
print(l[2:5]) #affiche les elts. de la position 2 a la position 4 (le dernier chiffre est exclu)

print(l[2]) #affiche le 2eme elt en partant du debut
print(l[-2]) #affiche le 2eme elt en partant de la fin


#------------------Modifier les elts. d'une liste------------------#


l[2] = "Guigui"
print(l[:])

l[:2] = ["Big G","Big Y"]
print(l[:])

l[:] = ["Jesus"] * len(l)
print(l[:])


#------------------Recherche dans une liste------------------#


if "Jesus" in l:
    print("Thanks god")
else:
    print("We're doomed")


#------------------Ajouter des objets a ma liste------------------#
    

l.append(True) #Ajoute un objet en fin de liste
print(l[:])

l.insert(2,"Gustave") #Ajouter a un endroit specifique
print(l[:])


#------------------Supprimer des elts.------------------#


l.remove("Jesus") #par un terme (ne supprime que la premiere occurence)
print(l[:])

del l[1] #par l'indice
print(l[:])

print(l.index(True)) #retourne l'index a laquel se trouve la premiere occurence de l'obj.


#------------------Reorganiser ma liste------------------#


l = [12,-3,435,-24,456,7]
l.sort()
print(l[:])

l.reverse() #inverser tt les elts. de ma liste
print(l[:])


#------------------Compter le nombre d'occurence d'un terme------------------#

l.append(7)
print("Nombre de 7 : {}".format(l.count(7)))


#------------------Effacer une liste------------------#


l.clear()
print(l[:])


#------------------De string a liste et inversement------------------#


string = "Ma chaine de caractere est magnifique"

l = string.split()
print(l[:])

string2 = " ".join(l) #Methode liee a une chaine de caractere
print(string2)


#------------------!!!Attention!!!------------------#


liste1 = ["Arc","Epee","Potion"]
#liste2 = liste1 --> Cree un lien direct entre liste 2 et liste 1, pas une copie

#Mais comment faire alors ?

import copy

liste2 = copy.deepcopy(liste1) #on cree une copie de la liste 1
liste2.append("Cape")
print(liste1[:])
print(liste2[:])


#------------------Concatener 2 listes------------------#


liste1 += liste2
print(liste1[:])
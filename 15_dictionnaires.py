
#15 Dictionnaires

"""
    Creation d'un dictionnaire : 

        dico = {} #vide
        dico = {<cle>:<valeur>,<cle2><valeur2>...}

    Acces a une valeur :

        dico[<cle>]

    Modifier / Ajouter une valeur :

        dico[<cle>] = <valeur>

            la cle existe       -> la valeur est modifiee
            la cle n'existe pas -> creation du nouvel item

    Supprimer un couple <cle><valeur> :

        dico.pop(<cle>)
        del dico[<cle>] 
"""

#Verifier l'existance d'une cle

dico = {"cle":"valeur","cle2":"valeur2","cle3":"valeur3","cle4":"valeur4"}

if "cle0" in dico:
    print("oui")
else:
    print("non")

#Parcourir mon dictionnaire

#afficher les cles
for key in dico.keys(): 
    print(key)

#afficher les valeurs
for value in dico.values():
    print(value)

#afficher les deux
for k,v in dico.items():
    print("Cle : {}, valeur : {}".format(k,v))


#Creer une copie d'un dictionnaire
dico2 = dico.copy()

#Parametres nommes
def funct(**parametres):
    # *  -> nombre variable de parametres
    # ** -> les parametres doivent etre obligatoirement nommes
    print(parametres) 

funct(b="yo", a="comment tu vas?") 
# retourne un dictionnaire
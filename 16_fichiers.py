
#16 Fichiers

"""
    modes d'ouvertures : 
    
        r -> lecture seule
        w -> ecriture avec remplacement
        a -> ecriture avec ajout en fin de fichier
        x -> lecture et ecriture

    lecture :

        read      -> tout le fichier
        readline  -> une seule ligne
        readlines -> le reste des lignes non lus

    ecriture :
"""
"""
#LECTURE

fic = open("16_fichiers.txt","r")

all = fic.read() # -> lire tout le fichier
print(all)

fic.close()


#ECRITURE

fic = open("16_fichiers.txt","a")

fic.write("Promete\n")

fic.close()
"""

"""
"""


import pickle

class Player:

    def __init__(self, name,level):
        self.name=name
        self.level=level

    def whoami(self):
        print("{} ({})".format(self.name, self.level))

p1 = Player("Kamski",12)

file=open("16_fichiers.txt","wb") # wb --> Ecriture en binaire

record = pickle.Pickler(file)
record.dump(p1)

file.close()


file = open("16_fichiers.txt","rb") # rb --> lecture binaire

get_record = pickle.Unpickler(file)
player1 = get_record.load()

file.close()

player1.whoami()
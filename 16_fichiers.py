
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

#LECTURE

fic = open("16_fichiers.txt","r")

all = fic.read() # -> lire tout le fichier
print(all)

fic.close()


#ECRITURE

fic = open("16_fichiers.txt","a")

fic.write("Promete\n")

fic.close()
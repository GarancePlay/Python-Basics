
#09 Methodes

class Humain:

    location = "Earth"

    """
        Constructeur
    """

    def __init__(self, nom, sexe, age):
        self.nom = nom
        self.sexe = sexe
        self.age = age

    """
        Construction d'une methode standard :

            -contient le parametre 'self'
            -Necessite l'instanciation d'un objet

    """

    def say(self, message):
        print("{} : {}".format(self.nom,message))

    """
        Construction d'une methode de classe :

            -contient le parametre 'cls'
            -Ne necessite pas l'instanciation d'un objet

    """   

    def change_location(cls,location):
        Humain.location = location
    change_location = classmethod(change_location)

    """
        Construction d'une methode static :

            -Ne contient ni 'cls' ni 'self'
            -Ne necessite pas l'instanciation d'un objet
            -Methode utilitaire qui n'atlere pas la classe elle meme
            -Peut etre appele depuis n'import ou

    """   

    def addition(a,b):
        print(a+b)

    add = staticmethod(addition)
    

#Programme principal
        
h1 = Humain("Garance","F",22)
h1.say("Hello world :)")

print(Humain.location)
Humain.change_location("Mars")
print(Humain.location)

Humain.add(12,45)
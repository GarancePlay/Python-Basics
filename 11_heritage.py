
#11 Heritage


#Classe mere 2
class Felin:
    pass

#Classe mere 1
class Animal:

    def __init__(self,nom):
        self.name=nom

    def se_deplacer(self):
        print("{} se deplace".format(self.name))

    def parler(self):
        print("RWW!")
    
"""
"""

#Classe fille
class Chat(Animal, Felin):
    #Heritage multiple

    def __init__(self, nom, race):
        Animal.__init__(self, nom)
        self.race = race
        
    def parler(self):
        print("Miaou")

"""
"""

#Programme principal
chat = Chat("Happy","Siamois")
print(chat.name)
chat.se_deplacer()
chat.parler()

if isinstance(chat,Chat):
    print("{} est un chat".format(chat.name))

if issubclass(Chat, Animal):
    print("Chat inherite Animal")


"""
    Fonctions utiles : 
            isinstance(<objet> , <classe>)           -> verifie qu'un objet est de la classe renseignee
            issubclass(<classe fille> , <classe mere>) -> verifie qu'une classe est fille d'une autre
"""
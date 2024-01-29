
#08 Classes et attributs

class Humain:

    humains_crees = 0

    def __init__(self, prenom, sexe, age): #constructeur
        self.name = prenom
        self.age = age
        self.gender = sexe
        Humain.humains_crees += 1


h1 = Humain("Garance","F",22)
print("Name : {}".format(h1.name))
print("Gender : {}".format(h1.gender))

h1.age = 23
print(h1.age)

#pas de getters / setters comme en Java / C# / C++

print(Humain.humains_crees)
h2 = Humain("Kamski","NB",29)
print(Humain.humains_crees)

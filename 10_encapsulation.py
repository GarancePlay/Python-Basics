
#10 Proprietes d'encapsulations

class Human:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def _getAge(self):
        try:
            return self._age
        except AttributeError:
            print("Doesn't exist!")

    def _setAge(self, new_age):
        if new_age < 0 :
            self._age = 0
        else :
            self._age = new_age

    #property(<getter>, <setter>)
    age = property(_getAge, _setAge)


#Programme principal

h1 = Human("Garance", 22)
print(h1.age)

h1.age = -5
print(h1.age)


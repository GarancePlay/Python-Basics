
#12 Chaines de caracteres

"""
    Une methode de chaine travaille sur une copie, et pas sur la chaine elle meme

    str.upper()         : tt en majuscule
    str.lower()         : tt en minuscule
    str.capitalize()    : premiere lettre en majuscule
    str.title()         : tt les premieres lettres de mot en majuscule

    str.center(<largeur>,<caractere_remplissage>)

    str.find(<chaine>)

        retour -1 si la chaine n'est pas trouvee
        retourne l'entier a partir duquel la chaine a ete trouve

    str.index(<chaine>)

        meme principe que str.find mais retourne une exception 
        si la chaine n'est pas trouvee

    str.strip() : retire tous les espaces avant et apres la chaine de caractere

    str.replace(<ancien charactere>,<nouveau caractere>,[<occurences>]) : 
    
        dans la chaine, remplace l'ancien caractere par le nouveau, 
        soit pour toute la chaine, soit pour un nombre d'occurence donne
"""

ma_chaine = "Bonjour tout le monde"

print(ma_chaine.upper())
print(ma_chaine.lower())
print(ma_chaine.capitalize())
print(ma_chaine.title())
print(ma_chaine.center(50,"-"))


print(ma_chaine.find("Tout"))


try:
    print(ma_chaine.index("Tout"))
except ValueError:
    print("La chaine n'a pas ete trouvee!")


string2 = "ababababab"
print(string2)
string2 = string2.replace("a","z",3)
print(string2)


"""
    transformer une chaine de caractere en liste
"""

string3 = "Magicien|PV : 10|MANA : 325"
print(string3.split("|"))


"""
"""

ch="Le langage python"

if "python" in ch:
    print("Trouve!")
else:
    print("Pas trouve!")


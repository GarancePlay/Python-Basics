
#03 coonditions


id = "GarancePlay"
passwd = "HKmp5sd101."

print("Interface connection\n")
user_id = input("Entrer username : ")
user_passwd = input("Enter password : ")

if (user_id == id and user_passwd == passwd):
    print("welcome",user_id,",you've successfully loged in!")
else :
    print("ID or password incorrect")


"""
    Operateurs de comparaison :
        == egal
        != different
        <  plus petit que
        >  plus grand que
        <= inferieur ou egal
        >= supperieur ou egal

    Mot cles de condition 
        if / elif / else

        and ET
        or  OU
        in  DANS
        not in PAS DANS
"""


lettre_hasard = input("Entrez une lettre : ")

if lettre_hasard in "aeiouy":
    print("C'est une voyelle")
else :
    print("C'est une consonne")


isLoaded = True

if isLoaded:
    print("Game loaded")
else:
    print("Game not loaded")


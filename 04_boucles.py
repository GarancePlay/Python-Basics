
#04 boucles


"""
    Boucles : while / for
    Mots cles : break (casse la boucle)
                continue (revient au debut de la boucle)
"""


i = 0
while i<5:
    print("ligne ",i+1)
    i+=1

is_running = True

while is_running:

    choix_menu = input("> ")
    if choix_menu == "again":
        continue
    elif choix_menu == "stop":
        is_running = False
    else:
        print("commande introuvable")

print("A bientot...")


"""
"""


phrase = "Deus ex machina"

for letter in phrase:
    print(letter)


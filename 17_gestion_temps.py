
#17 Gestion du temps

import time

#1er janvier 1970 --> timestamp
print(time.time())

begin = time.time()
print("Debut")

time.sleep(1)

end = time.time()
print("Fin")

print("Il s'est ecoule {} sec".format(end-begin))


"""
            localtime()
(TIMESTAMP) ---------> STRUCTURE DE TEMPS
            <---------
             mktime()
"""


tls = time.localtime()
print(tls)
tls = time.mktime(tls)
print(tls)


"""
    %d -> jours (1 - 31)
    %m -> mois (1 - 12)
    %Y -> annee
    %H -> heure
    %I -> minute
    %S -> seconde
    %p -> AM/PM

    %A -> jour semaine
    %B -> mois

    %Z fuseau horaire
"""

print(time.strftime("%Z"))


#18 Dates

import datetime


#dates completes
d1 = datetime.datetime(2077,1,31,4,51,37)
d2 = datetime.datetime(2024,1,31,4,51,37)
print(d1)

if d1  < d2 : # --> Possibilite de comparer 2 dates
    print("d1 est plus ancien que d2")
else :
    print("d1 est moins ancien que d2")

print(d1.year)

now = datetime.date.today()
print(now)

#heures
t1 = datetime.time(23,00,12)
print(t1)


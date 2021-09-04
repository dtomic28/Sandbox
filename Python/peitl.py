"""
import random

vnos1 = int(input("vnesite stevilo"))
vnos2 = int(input("vnesite stevilo"))
stetje = 0
while stetje != 10:
    ran = random.randint(vnos1, vnos2)
    print(ran)
    stetje += 1
"""
"""
import random

sez = []
stetje = 0
while stetje != 20:
    ran = random.randint(1,6)
    print(ran)
    sez.append(ran)
    stetje += 1
print("Povprečje je: " + str(sum(sez) / len(sez)))
"""

import random
print("Računalnik izbere število med -1000 in 1000. Vnašajte števila dokler ne izberete pravilno število")
ran = random.randint(-1000, 1000)

while True:
    vnos = int(input("Ugibajte stevilo"))
    if vnos == ran:
        print("Uganili ste število")
        break
    elif vnos < ran:
        print("Stevilo, ki ga iscete je vecje kot vneseno stevilo")
    elif vnos > ran:
        print("Stevilo, ki ga iscete je manjse kot vneseno stevilo")

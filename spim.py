
vnos = input("Vnesite stevilo: ")

for x in range(len(vnos)):
    vrstica = ""
    for y in range(len(vnos)):
        if y<=len(vnos)/3 and x<=len(vnos)/3 or x>len(vnos)/3 and y>len(vnos)/3:
            vrstica += vnos[y] + " "
        else:
            vrstica += "0 "
    print(vrstica)

"""
vnos = int(input("Vnesite st: "))
for i in range(vnos):
    vrstica = ""
    for j in range(vnos):
        if vnos/2==i-1:
            vrstica += "0 "
        else:
            vrstica += "1 "
    print(vrstica)
"""



vnos = int(input("Vnesite st: "))

for x in range(vnos):
    vrstica = ""
    for y in range(vnos):
        if x==y:
            vrstica += str(x) + " "
        else:
            vrstica += ". "
    print(vrstica)

print("-------------------------")

for x in range(vnos):
    vrstica = ""
    for y in range(vnos):
        vrstica += str(y) + " "
    print(vrstica)
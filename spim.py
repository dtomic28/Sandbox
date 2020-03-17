vnos = int(input("Vnesite stevilo: "))

for x in range(vnos):
    vrstica = ""
    for y in range(vnos):
        if y<=vnos/3 and x<=vnos/3 or x>vnos/3 and y>vnos/3:
            vrstica += "1 "
        else:
            vrstica += "0 "
    print(vrstica)
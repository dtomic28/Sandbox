def aliJeHarshadovoStevilo(x):
    y = x
    vsota = 0
    while x>0:
        stevka = x%10
        vsota += x
        x = x//10
    if y%x==0:
        print("True")
    else:
        print("false")

vnos = int(input("Vnesite stevilo: "))

print(aliJeHarshadovoStevilo(vnos))


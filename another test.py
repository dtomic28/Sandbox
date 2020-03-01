def najdiPrijatelja(N):
    vsota = 0
    for i in range(1,N):
        if N%i==0:
            vsota += i
            return vsota

x = int(input("Vnesite stevilo x: "))

najdiPrijatelja(x)
y = vsota

najdiPrijatelja(y)



if x==y:
    print("Da njen prijatelj je:",y)
else:
    print("Nima prijatelja")


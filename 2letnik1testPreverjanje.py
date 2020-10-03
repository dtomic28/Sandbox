#1 naloga

def pomoc(A):
    rezultat = 0
    for i in range(A,0,-2):
        rezultat += i
    return rezultat

def nekajCudnega(N):
    rezultat = pomoc(N) + pomoc(N-1)
    print(rezultat)

#2. naloga

def prestejAAje(datoteka):
    dat = open(datoteka, "r")
    datR = dat.read()
    c = 0
    for i in range(len(datR)):
        if datR[i:i+1] == "aa":
            c += 1
    return c

#3. naloga

def stevila(imeDat):
    dat = open(imeDat, "r")
    datR = dat.read().splitlines()
    c = 0
    for i in datR:
        c += i
    return c/len(datR)

#4. naloga
def kvadrat(beseda):
    pass


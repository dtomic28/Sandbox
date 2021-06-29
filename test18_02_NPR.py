def rekurzija(n):
    if n==1:
        return 4
    else:
        return 4*rekurzija(n-1)

def povprecnaCena(lisst):
    avg = 0
    for i in lisst:
        avg += i
    return avg/len(lisst)

def kvadrat(niz):
    for i in range(len(niz)):
        vrstica = ""
        for j in range(len(niz)):
            if i+j == len(niz) or i==j or len(niz)//2 == i or len(niz)//2 == j:
                vrstica += "1 "
            else:
                vrstica += "0 "
        print(vrstica)
            


def podraživev(seznam,odstotek):
    sez = []
    for i in seznam:
        j = i + i*(odstotek*0.01)
        sez.append(j)
    return sez



def kateraVelikostManjka(seznam):
    niz = ""
    if 1 not in seznam:
        niz += "majhna"
    if 2 not in seznam:
        if niz == "":
            niz += "obicajna"
        else:
            niz += "-obicjna"
    if 3 not in seznam:
        if niz == "":
            niz += "velika"
        else:
            niz += "-velika"
    if seznam == [1,2,3]:
        return 0
    return niz



def vsePice(picerija, seznamPic):
    if len(seznamPic) == 0:
        return 0
    else:
        if seznamPic[0].picerija == picerija:
            return 1 + vsePice(picerija, seznamPic[1:])
        else:
            return 0 + vsePice(picerija, seznamPic[1:])

sez = [1,2,4]

def rekurzija(sez):
    if len(sez) == 0:
        return
    else:
        if sez[0] == 1:
            print("gace")
        rekurzija(sez[1:])

rekurzija([1,2,2,1,1,2])
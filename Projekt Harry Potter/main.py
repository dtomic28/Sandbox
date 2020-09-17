def meni():
    pass

def izpisLika(ime):
    datoteka = open("HP_liki.csv", "r")
    vrstice = datoteka.read()
    l = vrstice.splitlines()
    for i in l:
        li = i.split(";")
        if ime in li[1]:
            p = li
            break
    datoteka.close()
    print(p[2], p[3], p[4])
    

def vnosNovegaLika():
    pass

def steviloCitatov(id):
    datoteka = open("HP_liki.csv", "r")
    datotekaR = datoteka.read().splitlines()
    for i in datotekaR:
        l = i.split(";")
        if id == l[0]:
            ime = l[1]
            break
    datoteka.close()
    datoteka = open("HP_citati.csv", "r")
    datotekaR = datoteka.read().splitlines()
    

def likiBrezCitatov():
    datoteka1 = open("HP_citati.csv", "r")
    datoteka1read = datoteka1.read().splitlines()
    datoteka2 = open("HP_liki.csv", "r")
    datoteka2read = datoteka2.read().splitlines()
    for i in datoteka2read:
        l1 = i.split(";")
        for j in datoteka1read:
            try:
                if l1[1] in j:
                    break
            except IndexError:
                pass
        else:
            print(l1[1])
    datoteka1.close()
    datoteka2.close()

def likiGledeNaHiso(hisa):
    datoteka = open("HP_liki.csv", "r")
    vrstice = datoteka.read()
    vrstice_split = vrstice.splitlines()
    l = []
    for i in vrstice_split:
        li = i.split(";")
        try:
            if hisa in li[4]:
                print(li[1])
        except IndexError:
            pass
    datoteka.close()

likiBrezCitatov()
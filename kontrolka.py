def podvojiObrat(niz):
    novNiz = ""
    for i in range(len(niz)-1, -1, -1):
        stetje = 0
        while stetje!=2:
            novNiz += niz[i]
            stetje += 1
    print(novNiz)

def izberiSog(niz):
    novNiz = ""
    soglasniki = ["a", "e", "i", "o", "u"]
    for crke in niz:
        if crke in soglasniki:
            novNiz += crke
    print(novNiz)

def kvadrat(beseda):
    for i in range(len(beseda)):
        vrstica = ""
        for j in range(len(beseda)):
            if i<=len(beseda)/3 and j<=len(beseda)/3 or j>len(beseda)/3 and i>len(beseda)/3:
                vrstica += "0 "
            else:
                vrstica += beseda[i] + " "
        print(vrstica)

def prestejPodniz(niz, podniz):
    while stetje!=len(niz):
        stetje = 0

kvadrat("beseda")
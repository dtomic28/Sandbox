def dodajObrat(niz):#definiramo podpogram dodaj obrat
    obrnjeno = niz[::-1]#stevilo obrnemo z pomocjo spremenljivke
    print(niz + obrnjeno) #izpisemo neobrnjen niz in obrnjen niz

dodajObrat("avto")

def podvojiZnake(zacetniNiz):
    izpis = "" 
    for znaki in zacetniNiz: 
        for i in range(2): 
            izpis += znaki 
    print(izpis)

podvojiZnake("avto")

def podvojiSamoglasnike(zacetniNiz): 
    samoglasniki = ["a","e","i","o","u"] 
    izpis = "" 
    for i in zacetniNiz: 
        if i in samoglasniki: 
            stetje = 0 
            while stetje!=2: 
                izpis += i 
                stetje += 1 
        else:
            izpis += i 
    print(izpis) 

podvojiSamoglasnike("avto")

                
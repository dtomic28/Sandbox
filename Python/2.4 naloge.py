def razlicneStevilke(seznam): #definiramo podmetodo razlicne stevilke ki sprejemejo vhodni seznam
    s = set()#ustvarimo množico
    for items in seznam: #za vsako element v seznamu
        if items%2!=0: #če je liho
            s.add(items) #ga dodamo v množico
    print(len(s))#izpišemo koliko lihih elemtov je

def skupneBesede(sez1, sez2): #definiramo podmetodo skupneBesede z vhodnimi seznami 
    s = set() #ustvarimo množico
    for items in sez1: #za vsak element v seznamu
        if items in sez2: #če je v drugem seznamu
            s.add(items) #ga dodamo v množico
    for s in s: #za vsak element v množici
        print(s) #ga ispišemo
    
            

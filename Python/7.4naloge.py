def razlicnaImena(seznam): #definiramo podmetodo razlicnaImena z vhodno spremenljivko seznam
    m = set() #ustvarimo mnozico
    for e in seznam: #za vsak element v seznamu
        m.add(e.split()[0]) #Dodamo ime v množico
    print(m) #izpišemo množico

def razlicneCrke(niz): #definiramo podmetodo razlicne crke z vhodno spremenljivko niza
    abeceda = "abcdefghijklmnopqrstuvwxyz" #napišemo abecedo
    m = set(niz) #naredimo množico z vhodnim nizom
    print(list(set(abeceda).difference(m))) #izpišemo razliko z pomočjo funkcije difference množic



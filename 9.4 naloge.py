import re #importamo knjižnico re

def tehnica(stevila): #definiramo podmetodo tehnica z vhodnim seznamom stevila
    dv = set() #definiramo množico za dvomestna st
    tr = set() #definiramo množico za tromestna st
    for items in stevila: #za vsak elemennt v seznamu 
        if len(str(items))==2: #če je dvomestno število
            dv.add(items) #dodamo v množico za dvomestna st
        elif len(str(items))==3: #če je tromestno št
            tr.add(items) #dodamo v množico za tromestna št
    if len(dv) > len(tr): #če je več dvomestnih števil
        print('Bilo je vec dvomestnih stevil in sicer %d' %len(dv) ) #izpišemo da je dvomestnih več in koliko jih je
    elif len(dv) == len(tr): #če je enako št dvomestnih in tromestnih
        print('Bilo je enako stevilo dvomestnih in tromestnih stevil') #izpišemo da je tako
    else: #če je več tromestnih kot dvomestnih
        print('Bilo je več tromestnih števil in sicer %d' %len(tr)) #izpišemo da je več tromestnih in koliko jih je


def razlicneBesede(niz): #definiramo podmetodo razlicne besede z vhodnim nizom
    niz = niz.lower() #pretvorimo v male crke
    niz = re.split(', |_|-|!| ', niz) #razdvojimo niz v besede
    s = set(niz) #dodamo besede v množico
    print(s) #izpišemo množico


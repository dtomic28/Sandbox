def razlicanStevila(): #definiramo metodo razlicnaStevila 
    dic = {} #ustvarimo nov slovar
    while True: #naredimo neskončno zanko
        try: #poskusimo nek ukaz
            vnos = int(input('Vnesite stevilo: ')) #vnesemo število
        except ValueError: #če nam vrže error
            break #se bo zanka ustavila torej v primeru da ni število ali da je prazno
        if vnos not in dic: #če ni vnos v slovarju
            dic[vnos] = 1 #vnesemo število v slovar
    return len(dic) #izpišemo koliko različnih števil je v slovarju
 
def razlicniZnaki(poljunnoDolgoBesedilo): #definiramo podmetodo z vhodno spremenljivko niz
    dic = {} #ustvarimo nov slovar
    for c in poljunnoDolgoBesedilo: #za vsako crko v nizu
        if c not in dic and c!=' ': #če ni v slovarju in če ni presledek
            dic[c] = 1 #ga dodamo v slovar
    return len(dic) #izpišemo števila




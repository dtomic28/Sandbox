import random  #importamo knjižnico random

def sodoStevila(): #definiramo podmetodo sodoStevilo
    while True: #neskončna while zanka 
        n = random.randint(10,100) #spremenljivko n nastavimo na poljubno generirano stevko
        if n%2==0: #če je n sodo
            print(n) #se števka izpiše
            break #program se zaključi



def besede(seznamBesed): #definiramo podmetodo besede z vhodno spremenljivko seznam besed
    maxNiz = "" #max niz je prazen
    maxSt = 0 #max st nastavimo na 0
    minNiz = "" #min niz je prazen 
    minSt = 99999999999999 #min st je na nekem visokem številu 
    for items in seznamBesed: #za vsako besedo v seznamu besed
        if len(items)>maxSt: #če je dolžina večja kot prejšnja največja dolžina 
            maxSt = len(items) #maxSt nastavimo na najdalšo dolžino 
            maxNiz = items #max niz nastavimo na trenutno besedo
    for items in seznamBesed: #za vsako besedo v seznamu  
        if len(items)<minSt: #če je dolŽina besede večja kot prejšnja najmanša vrednost
            minSt = len(items) #minSt nastavimo na trenutno najmanjšo dolžino
            minNiz = items #minNIz nastavimo na trenuten najkrajši niz
    print("Največja vrednost je: %s" %maxNiz) #izpis najdalšega niza
    print("Najmanjša vrednost je: %s" %minNiz) #izpis najkrajšega niza


def najpogostejsaCrka(seznam):
    dic = {} #naredimo nov slovar
    for i in dic: #za vsako črko v seznamu
        for crke in i: #za vsako črko v besedi
            if crke not in dic: #če ni črka v slovarju 
                dic[crke]=1 #nastavimo vrednost ključa v tem primeru črka na 1
            else: #če je že v seznamu
                dic[crke]+=1 #povečamo za 1
    maximum = max(dic, key=dic.get) #dobimo najbolj pogosto črko v seznamu
    print(maximum) #in jo izpišemo



    
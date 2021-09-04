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

#prva

def prastevila(sez):
    l = []
    for items in sez:
        if items>1:
            for i in range(2, items):
                if items%i==0:
                    break
            else:
                l.append(i)   
    print(l)


def najpogostejseStevilo(sez):
    dic = {}
    for items in sez:
        if items not in dic:
            dic[items] = 1
        else: 
            dic[items] += 1
    maximum = max(dic, key=dic.get)
    print(maximum) 

def najpogostejsaBeseda(besedilo):
    besedilo = besedilo.split()
    dic = {}
    for items in besedilo:
        if items not in dic:
            dic[items] = 1
        else: 
            dic[items] += 1
    maximum = max(dic, key=dic.get) 
    print(maximum) 



        

def rekurzijaPrastevila(st):
    if st>1:
        for j in range(2, st):
            if st%j==0:
                rekurzijaPrastevila(st-1)
        else:
            print(st)
            rekurzijaPrastevila(st-1)
    else:
        print("konec")

def kvadrat(n):
    for i in range(n):
        vrstica = ""
        for j in range(n):
            if i==j:
                vrstica += "1 "
            else:
                vrstica += "0 "
        print(vrstica)

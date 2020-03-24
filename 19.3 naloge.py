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

def prastevila(seznamStevil):
    sez = []
    for i in seznamStevil:
        if i>1:
            for j in range(2, i):
                if i%j==0:
                    break
            else:
                sez.append(i)   
    print(sez)


#druga

def najpogostejseStevilo(seznamStevil):
    seznamStevil.sort()
    najPogostejeSt = 0
    najPogostejeSTEVKA = ""
    stetje = 0
    trenutna = "a"
    for i in seznamStevil:
        if i!=trenutna:
            stetje = 1
            trenutna = i
        if stetje > najPogostejeSt:
            najPogostejeSt = stetje
            najPogostejeSTEVKA = str(i)
        else:
            stetje += 1
    print(najPogostejeSTEVKA)
        

def najpogostejsaBeseda(besedilo):
    besedilo = besedilo.split()
    besedilo.sort()
    najPogostejeSt = 0
    najPogostejeSTEVKA = ""
    stetje = 0
    trenutna = "a"
    for i in besedilo:
        if i!=trenutna:
            stetje = 1
            trenutna = i
        if stetje > najPogostejeSt:
            najPogostejeSt = stetje
            najPogostejeSTEVKA = str(i)
        else:
            stetje += 1
    print(najPogostejeSTEVKA)



        

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

rekurzijaPrastevila(100)






        

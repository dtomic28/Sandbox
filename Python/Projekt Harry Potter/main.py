def meni(): #definiramo meni
    while True: #Neskončna zanka
        print("\nDobrodošli v program Harry Potter")
        print("Izberite Funkcije: ")
        print("1. Izpis Lika")
        print("2. Vnos novega lika")
        print("3. Število citatov")
        print("4. Liki brez citatov")
        print("5. Liki glede na hišo")
        print("6. Izhod")                           #izpišemo meni                       
        vnos = input("\nIzberite funkcijo: ") #izberemo funkcije
        if vnos == "1": #če izberemo funkcijo 1 dobimo izpis lika
            vnos1 = input("Vnesite ime lika: ")
            izpisLika(vnos1)
        elif vnos == "2": #če izberemo funkcijo 2 dobimo vnos novega lika
            vnos1 = input("Vnesite ime lika: ")
            vnos2 = input("Vnesite spol: ")
            vnos3 = input("Vnesite poklic lika: ")
            vnos4 = input("Vnesite hišo: ")
            vnos5 = input("Vnesite ime čarobne palice: ")
            vnos6 = input("Vnesite ime pokrivatelja: ")
            vnos7 = input("Vnesite sorto: ")
            vnos8 = input("Vnesite kri: ")
            vnos9 = input("Vnesite barvo las: ")
            vnos10 = input("Vnesite barvo oći: ")
            vnos11 = input("Vnesite zvestobo: ")
            vnos12 = input("Vnesite spretnosti: ")
            vnos13 = input("Vnesite datum rojstva: ")
            vnos14 = input("Vnesite datum smrti: ")
            vnosNovegaLika(vnos1, vnos2, vnos3, vnos4, vnos5, vnos6, vnos7, vnos8, vnos9, vnos10, vnos11, vnos12, vnos13, vnos14)
        elif vnos=="3": #če izberemo funkcijo 3 dobimo število citatov
            vnos1 = input("Vnesite id lika: ")
            steviloCitatov(vnos1)
        elif vnos=="4": #če izberemo funkcijo 4 izpišemo like brez citatov
            likiBrezCitatov()
        elif vnos == "5": #če izberemo funkcijo 5 dobimo like glede na hišo
            vnos1 = input("Vnesite ime hiše: ")
            likiGledeNaHiso(vnos1)
        elif vnos == "6": #Če izberemo 6 izberemo izhod in se zanka zaustavi
            break
    



def izpisLika(ime): #definiramo pomdetodo izpisLika z vhodno spremenljivko ime
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko z liki v načinu branja
    vrstice = datoteka.read() #vrstice preberemo
    l = vrstice.splitlines() #uporabimo metodo .splitlines()
    for i in l: #za vsako vrstico v seznamu
        li = i.split(";") #razdelimo vrstico v seznam
        try:
            if ime in li[1]: #če je ime v tisti vrstici kjer stojijo imena
                p = li #shranimo vrstico na spremenljivko p
                break #zaustavimo for znako saj smo našli vrstico
        except IndexError: #Če pride index error
            pass #ga preskočimo
    datoteka.close() #zapremo datoteko
    try: #poskusimo printati
        print(p[2], p[3], p[4]) #in izpišemo tiste podatke, ki jih rabimo izpisati
    except UnboundLocalError: #Če pride error 
        print("\nVneseni lik ne obstaja poskusite znova") #Pomeni, da vneseni lik ne obstaja
    

def vnosNovegaLika(name, gender, job, house, wand, patronaus,species, Blood, Hair, eyes, loyalty, skills, birth, death): #definiramo metodo Vnos novega lika z vsemi zahtevanimi podatki
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko v načinu branja
    datotekaR = datoteka.readlines() #preberemo datoteko
    zadnjiId = 0 #ustvarimo spremenljivko na katero bomo našli zadnji id
    for i in reversed(datotekaR): #z for zanko od konca gledamo za števila
        l = i.split(";") #vrstico razdelimo na seznam
        if l[0].isnumeric()==True: #če je id tam kjer mora biti
            zadnjiId = int(l[0]) #ga zapišemo 
            break #in zaključimo zanko
    datoteka.close() #datoteko zapremo
    datoteka = open("HP_liki.csv", "a") #Jo zopet opdremo v načinu dodajanja
    datoteka.write("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s\n" %(str(zadnjiId+1),name, gender, job, house, wand, patronaus,species, Blood, Hair, eyes, loyalty, skills, birth, death)) #zapišemo zahtevane podatke
    datoteka.close() #zapremo datoteko

def steviloCitatov(idd): #definiramo novo metodo steviloCitatov, ki ima vhodno spremenljivko id
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko v načinu branja
    datotekaR = datoteka.readlines() #preberemo datoteko
    zadnjiId = 0 #ustvarimo spremenljivko na katero bomo našli zadnji id
    for i in reversed(datotekaR): #z for zanko od konca gledamo za števila
        l = i.split(";") #vrstico razdelimo na seznam
        if l[0].isnumeric()==True: #če je id tam kjer mora biti
            zadnjiId = int(l[0]) #ga zapišemo 
            break #in zaključimo zanko¸
    datoteka.close() #Datoteko zapremo saj je ne rabimo več
    if int(idd) > zadnjiId: #Pogledamo če je vneseni id večji kot največji id
        print("Vnesli ste ID, ki ne obstaja") #Če je izpišemo, da je napačno vneseno
        return #In vnremo
    ime = "" #naredimo prazno spremenljivko za ime
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko v načinu za branje
    datotekaR = datoteka.read().splitlines() #preberemo datoteko damo vrstice v seznam
    for i in datotekaR: #za vsako vrstico
        l = i.split(";") #razdelimo vrstico na seznam
        if str(idd) == l[0]: #če je id v prvi celici seznama, kjer imamo formatirano id
            ime = l[1] #ime shranimo za poznejšo uporabo
            break #zaustavimo for zanko
    datoteka.close() #datoteko zapremo
    datoteka = open("HP_citati.csv", "r") #odpremo drugo datoteko v načinu branja
    datotekaR = datoteka.read().splitlines() #datoteko isto preberemo in damo vrstice v seznam
    najdalsi = [] #ustvarimo seznam na katerega bomo shranjevali vse citate in izbrali najdaljšega
    for i in datotekaR: #gremo skozi vsako vrstico v datoteki
        l = i.split(";") #vsako vrstico spremenimo v seznam
        try: #uporabimo try, da nam gre skozi tudi če pokaže error
            if ime in l[1]: #če je ime v celici kjer so imena
                najdalsi.append(l[2]) #dodamo citat na seznam
        except:  #če je error
            pass #ga preskočimo
    try: #Poskusimo izpisati
        print(len(najdalsi), "\nNajdaljsi citat je: %s" %max(najdalsi, key=len)) #izpišemo koliko citatov je bilo in kateri je najdaljši
    except ValueError: #Če pride error 
        print("Izbrani lik nima nobenega citata ali pa ne obstaja") #Pomeni, da lik ne izreče citata ali ne obstaja
    datoteka.close() #zapremo drugo datoteko

def likiBrezCitatov(): #ustvarimo novo metodo likiBrezCitatov, ki nima nobenih vhodnih agrumentov
    datoteka1 = open("HP_citati.csv", "r") #odpremo prvo datoteko v načinu branja
    datoteka1read = datoteka1.read().splitlines() #jo preberemo
    datoteka2 = open("HP_liki.csv", "r") #odpremo drugo datoteko v načinu branja
    datoteka2read = datoteka2.read().splitlines() #preberemo drugo datoteko
    for i in datoteka2read: #za vsako vrstico v prebrani datoteki z liki
        l1 = i.split(";") #vrstico razdelimo v seznam
        for j in datoteka1read: #ustvarimo novo for znako ki gre skozi 1. datoteko, ki išče citate
            try: #poskusimo najti citat 
                if l1[1] in j: #če je v citatih
                    break #prekinemo zanko
            except IndexError: #če pride error
                pass #ga preskočimo
        else: #če se for zanka ne ustavi in gre skozi
            try:
                print(l1[1]) #izpišemo lika
            except IndexError:
                pass
    datoteka1.close() #zapremo obe datoteki
    datoteka2.close() #-||-

def likiGledeNaHiso(hisa): #definimramo metodo likiGledeNaHiso z vhodno spremenljivko hisa
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko o likih v načinu za branje
    vrstice = datoteka.read() #preberemo vrstice
    vrstice_split = vrstice.splitlines() #razdelimo vrstice v seznam
    for i in vrstice_split: #gremo skozi seznam vrstic
        li = i.split(";") #vrstice razdelimo na seznam
        try: #poskusimo če bo error
            if hisa in li[4]: #če je ime hiše tam kjer so imena hiš
                print(li[1]) #izpišemo ime
        except IndexError: #če je error
            pass #ga preskočimo
    datoteka.close() #zapremo datoteko

meni()#Pokličemo meni oz cel program
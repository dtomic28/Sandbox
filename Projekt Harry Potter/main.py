def meni():
    pass

def izpisLika(ime): #definiramo pomdetodo izpisLika z vhodno spremenljivko ime
    datoteka = open("HP_liki.csv", "r") #odpremo datoteko z liki v načinu branja
    vrstice = datoteka.read() #vrstice preberemo
    l = vrstice.splitlines() #uporabimo metodo .splitlines()
    for i in l: #za vsako vrstico v seznamu
        li = i.split(";") #razdelimo vrstico v seznam
        if ime in li[1]: #če je ime v tisti vrstici kjer stojijo imena
            p = li #shranimo vrstico na spremenljivko p
            break #zaustavimo for znako saj smo našli vrstico
    datoteka.close() #zapremo datoteko
    print(p[2], p[3], p[4]) #in izpišemo tiste podatke, ki jih rabimo izpisati
    

def vnosNovegaLika():
    datoteka = open("HP_liki.csv", "a")
    datotekaR = datoteka.readlines
    
    

def steviloCitatov(idd): #definiramo novo metodo steviloCitatov, ki ima vhodno spremenljivko id
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
    print(len(najdalsi), "\nNajdaljsi citat je: %s" %max(najdalsi, key=len)) #izpišemo koliko citatov je bilo in kateri je najdaljši
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
            print(l1[1]) #izpišemo lika
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

steviloCitatov(3)
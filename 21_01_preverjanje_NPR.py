class skladba: #definiramo razred skladba

    def __init__(self, naslov, drzava, izvajalec, avtorBesedila, avtorGlasbe, dolzina, besedilo,zastava, leto, stDosezenihTock): #naredimo konstruktor z vsemi navedenimi podatki
        self.naslov = naslov
        self.drzava = drzava
        self.izvajalec = izvajalec
        self.avtorBesedila = avtorBesedila
        self.avtorGlasbe = avtorGlasbe
        self.dolzina = dolzina
        self.besedilo = besedilo
        self.zastava = zastava
        self.leto = leto
        self.stDosezenihTock = stDosezenihTock

    def cenzura(self,sez): #definiramo metodo ceznura z vhodno spremembo seznam
        l = self.besedilo.split(" ") #naredim seznam iz niza
        nov = '' #naredim nov niz
        for i in l: #za vsak element v seznamu
            if i in sez: #pogledamo, če je v seznmu kjer so besede, ki se rabijo cenzurirati
                i = '#' * len(i) #zamenjamo z cenzurirano besedo
            nov += i + " " #dodamo na novniz in dodamo presledek
        print(nov) #izpišemo novniz

    def obrniImeInPriimek(self): #ustvarimo metodo obrniimeinpriimek
        if len(self.izvajalec) == 0: #če je konec rekurzije 
            return "" #vrnemo prazen niz
        else: #če še ni konec
            return obrniRec(self.izvajalec[1:]) + self.izvajalec[0] #se poglobimo v rekurzijo

    def steviloBesed(self):#ustvarimo metodo stevilo besed 
        besed = self.besedilo #naredimo nov niz, ki zato da nebomo spreminjali orginalnega
        for i in [",", "."]: #za vsak el. v sez
            besed = besed.replace(i, "") #ga odstranimo
        sez = besed.split(" ") #niz damo v seznam
        return len(set(sez)) #nato damo seznam v set in vrnemo dolžino

sez = [] #ustvarimo prazen seznam
def shraniPodatke(N): #ustvarimo seznam shrani podatke z vhodno spremenljivko N
    global sez #naredimo globalen seznam
    while len(sez) != N: #zanka gre dokler nebo n objektov
        vnos1 = input("Vnesite naslov: ")#Vnesemo vse podatke
        vnos2 = input('Vnesite drzavo: ')
        vnos3 = input('Vnesite izvajalca: ')
        vnos4 = input('Vnesite avtorja besedila: ')
        vnos5 = input("Vnesite avtorja glasbe: ")
        vnos6 = int(input("Vnesite dolžino skladbe v sekundah: "))
        vnos7 = input('Vnesite besedilo: ')
        vnos8 = int(input('Koliko števil hočete v seznamu? '))
        s = []
        for i in range(vnos8):
            vnos = int(input('Vnesite št: '))
            s.append(vnos)
        vnos9 = int(input('Vnesite leto nastopa: '))
        vnos10 = int(input('Vnesite število doseženih točk'))
        sez.append(skladba(vnos1, vnos2, vnos3, vnos4, vnos5, vnos6, vnos7, s, vnos9, vnos10 )) #ustvarimo objekt

def razlicneZvrsti(seznamIger): #definiramo metodo razlicne zvrsti
    s = set() #ustvarimo set
    for i in seznamIger: #pogledamo po seznamu iger
        set.add(i.zvrst) #dodamo zvrst v set
    for i in s: #gremo skozi set
        print(i) #in izpišemo

def cenzura(self, sez):
    for i in sez:
        self.besedilo.replace(i, "#" * len(i))
    print(self.besedilo)
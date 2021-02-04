import random #Vnesemo knjižnjico ranodm

class Bitje: #ustvarimo razred bitje
    def __init__(self,imeBitja,tipBitja,zaporednaStevilka,zivljenjskeTocke,mocNapada): #naredimo metodo konstruktor z ime, tip, zaporedne stevilke, zivljenske tocke in moc napada
        self.imeBitja=imeBitja #ime bitja
        self.tipBitja=tipBitja #ena izmed moˇznosti: clovek, vilinec, skrat, carovnik
        self.zaporednaStevilka=zaporednaStevilka #stevilo v trojiskem st. sestavu
        self.zivljenjskeTocke=zivljenjskeTocke #naravno stevilo med 0 in 100
        self.mocNapada=mocNapada #naravno stevilo med 5 in 50

    def poskodba(self, napad): #ustvarimo metodo poskodba, ki sprejme napad
        self.zivljenjskeTocke -= napad #odštejemo točke napada od hpja

    def vrniZapStevilo(self, napad): #Ustvarimo metodo, ki vrne besedilo iz trojiskega v desetisko
        pot = len(self.zaporednaStevilka)-1 #dobimo potenco iz dolzine stevila
        t = 0 #ustvarimo spremenljivko za stetje
        for i in self.zaporednaStevilka: #za vsako stevko v trojiskem stevilu
            t += int(i) * (3**pot) #dodamo potenco pomnoženo z stevko
            pot -= 1 #potenco odstejemo 
        return t #vrnemo t

    def __str__(self): #ustvarimo metodo __str__, ki pove, ko izpišemo objekt kaj
        return('%d - %s[%s] Zivljenje: %d, Napad: %d' %(self.vrniZapStevilo(self.zaporednaStevilka), self.imeBitja, self.tipBitja, self.zivljenjskeTocke, self.mocNapada))

    def preveriZapStevilo(self): #ustvarimo metodo, ki preveri ali je stevilo trojisko
        for i in self.zaporednaStevilka: #za vsako stevko v nizu
            if i not in ['1','2','0']: #vemo, da trojiska stevila lahko imajo samo 1 2 ali 0 zato, če je kaj drugega vrnemo false
                return False
        return True #drugače true

    def virus(self): #ustvarimo metodo virus
        s1 = "" #ustvarimo en niz za soda znake
        s2 = "" #in en za lihe znake
        for i in range(len(self.imeBitja)): #za vsak znak v imenu
            if i%2==0: #če je sodi
                s1 += self.imeBitja[i] #dodamo na sodo
            else: #drugače 
                s2 += self.imeBitja[i] #dodamo na lihe
        self.imeBitja = (s1 + s2) #združimo sode in lihe znake
        self.zivljenjskeTocke -= (self.zivljenjskeTocke/100) * 10 #odštejemo 10% od hp
        self.mocNapada -= (self.mocNapada/100) * 10 #in 10% od napada
    
    def __repr__(self): #ustvarimo metodo __repr__, ki služi podoben pomen kot __Str__ vendar, da če imamo objekt v seznamu nam pokaže tako kot dabi ga izpisali namesto kje se nahaja na pomnilniku
        return('%d - %s[%s] Zivljenje: %d, Napad: %d' %(self.vrniZapStevilo(self.zaporednaStevilka), self.imeBitja, self.tipBitja, self.zivljenjskeTocke, self.mocNapada))


sez1 = [] #ustvarimo 1 seznam
sez2 = [] #ustvarimo drug seznam
def shraniPodatke(n): #ustvarimo metodo, ki shrani podatke
    global sez1, sez2 #uporabimo globalne spremenljivke
    f = 0 #ustvarimo flag
    while len(sez2) != n: #dokler nista oba seznama napolnjena 
        vnos1 = input('Vnesite ime bitja: ') #vnos za ime bitja
        vnos2 = input('Vnesite tip bitja: ') #vnos za tip bitja
        vnos3 = input('Vnesite zaporedno številko: ') #vnos za zaporedno številko
        vnos4 = int(input('Vnesite življenske tocke: ')) #vnos za življenske točke 
        vnos5 = int(input('Vnesite moc napada: ')) #vnos za moč napada
        if f == 0: #če je flag na 0
            sez1.append(Bitje(imeBitja = vnos1, tipBitja = vnos2, zaporednaStevilka = vnos3, zivljenjskeTocke = vnos4, mocNapada= vnos5)) #ga shranimo pod sez1
        else: #drugače 
            sez2.append(Bitje(imeBitja = vnos1, tipBitja = vnos2, zaporednaStevilka = vnos3, zivljenjskeTocke = vnos4, mocNapada= vnos5)) #ga shranimo pod sez2
        f = (f+1)%2 #zamenjamo flag

def simulacijaBitke(seznam1, seznam2): #definiramo metodo simulacija bitke z vhodom dveh seznamov
    ind1 = 0 #ustvarimo spremenljivko. ki spremlja index igralcev
    ind2 = 0 
    f = 0 #usvrarimo flag
    while ind1 > len(seznam1)-1 or ind2 > len(seznam2)-1: #dokler igre ni konec
        if f == 0 or f == 2: #če je flag 0 ali 2
            seznam1[ind1].poskodba(seznam2[ind2].mocNapada) #igralca napadejo
            if seznam1[ind1].zivljenjskeTocke <= 0: #če je mrtev
                seznam1[ind1].zivljenjskeTocke = 0#spremenimo hp na 0 če je slučajno manj
                ind1 += 1 #izberemo naslednjega
        elif f == 1: 
            seznam2[ind2].poskodba(seznam1[ind1].mocNapada)
            if seznam2[ind2].zivljenjskeTocke <= 0:
                seznam2[ind2].zivljenjskeTocke = 0
                ind2 += 1
        f = (f+1)%3
        if f == 2:#če je čas za virus
            st_rand = random.randint(1,2) #izberemo random igralca
            st_ig = random.randint(1, len(seznam1)) #izberemo bitje od teh igralcev
            if st_rand == 1: #če je izbran igralec 1 mu damo virus
                seznam1[st_ig-1].virus()
            else: #če ne damo drugemu
                seznam2[st_ig-1].virus()
    if ind1 < ind2: #izpišemo igralca
        print('Igralec 1 je zmagovalec')
    else:
        print('Igralec 2 je zmagovalec')

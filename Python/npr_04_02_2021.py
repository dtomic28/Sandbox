def zaporedje(n): #defniniramo metodo zaporedje z vhodno spremenljivko n
    s = 1 #začnemo z številom 1
    start = 4 #začnemo dodajati 4 saj vsakiš ko dodamo povečamo spremenljivko za 2
    for i in range(n): #zanka se ponovi tolikokrat kolikor vnesemo
        s += start #prištejemo na štetje številko, za katero se povečuje
        start += 2 #številko ki povečuje povečjmao
    return s #vrnemo številko


def najpogostejsiZnak(niz): #definiramo metodo najpogostejsi znak z vhodno spremenljivko niz
    dic = {} #ustvarimo slovar
    for i in niz: #za vsak znak v nizu
        if i not in dic: #pogledamo če je v slovarju
            dic[i] = 1 #če ga še ni nastavimo njegovo vrednost na 1
        else: #v obratenm primeru da že je
            dic[i] += 1 #povečamo vrednost kolikokrat se pojavi za 1
    najvecja = "" #ustvarimo spremenljivko na katero bomo shranili kateri znak je najpogostejši
    najvecjaSt = 0 #ustvarimo spremenljivko na katero s katero bomo primerjali kolikokrat se ponovi
    for k,v in dic.items(): #za vsak ključ in vrednost v slovarju
        if v >= najvecjaSt: #pogledamo če je vrednost večja kakor največja prejšnja
            najvecja = k #jo shranimo
            najvecjaSt = v #in posodobimo na novo vrednost 
    return najvecja #in vrnemo najbolj pogosto

class skladba: #usvarimo razred skladba
    
    def __init__(self, naslov, leto, dolzina, zvrst, pevec, avtor): #nastavimo konstruktor
        self.naslov = naslov
        self.letoNastanka = leto
        self.dolzinaSkladbe = dolzina
        self.zvrstSkladbe = zvrst
        self.pevec = pevec
    
    def steviloSekund(self): #definiramo metodo, z vhodno spremenljivko self, kar pomeni da deluje na svoj objekt na katerem ga pokličemo
        s = int(self.dolzinaSkladbe[4:]) #indexiramo vrednost sekund iz niza in jih pretvorimo v celoštevilo
        s += int(self.dolzinaSkladbe[:2])*3600 #dodamo vrednost ur pomnoženo z 3600 saj toliko sekund je v uri in prištejemo sekundam
        s += int(self.dolzinaSkladbe[2:4])*60 #isto naredimo za minute vendar da pomnožimo s 60sekund
        return s #vrnemo vrednosti

    def vrniPriimek(self): #definiramo vrni priimek z vhodom self
        return(self.pevec.split(" ")[1]) #vrnemo 2. element seznama, ki ga naredimo tako da razcepimo niz na presledku

def najdaljsaSkladba(seznamSkladb): #definiramo metodo najdaljsa sklaba z vhodno spremenljivko seznam skladb
    najdaljsa = "" #ustvarimo spremenljivko, ki bo shranjevala sam naslov skladbe z najdaljso dolzino
    najdaljsaSt = 0 #usvraimo spremenljivko, ki bo shranjevala dolžino posamezne najdaljše pesmi
    for i in seznamSkladb: #za vsako skladbo na seznamu
        if i.steviloSekund > najdaljsaSt: #pogleda če je večja kot trenutna najdaljša skladba
            najdaljsaSt = i.naslov #če je shranimo naslov
            najdaljsaSt = i.steviloSekund #in novo dolžino
    return najdaljsa #vrnemo ime najdaljše skladbe

def starejseSkladbe(seznamSkladb, leto): #definiramo metodo starejseSkladbe, ki ima vhod leto in seznam skladb
    c = 0 #nastavimo spremenljivko, ki bo štela na 0
    for i in seznamSkladb: #pogledamo vsako pesem v seznamu
        if i.letoNastanka < leto: #če je starejša kot leto
            c += 1 #prištejemo na spremenljivko
    return c #vrnemo na c
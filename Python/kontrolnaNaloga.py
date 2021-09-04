def dvojiskaStevila(seznam):
    for i in seznam:
        
        sez = i.split("")
        print(sez)
    
#dvojiskaStevila([123,10001, 123214212421])

def najmlajsaKnjiga(naslov,leto):
    dic = {}
    for i in range(len(naslov)):
        if naslov[i] not in dic:
            dic[naslov[i]] = leto[i]
    naj = {"letoIzdaje": 0, "naslov": ""}
    for k,v in dic.items():
        if v > naj['letoIzdaje']:
            naj['letoIzdaje'] = v
            naj['naslov'] = k
    print("Najmlajsa knjiga je %s" %naj['naslov'])
        
def manjsiPokemoni(pokemoni, imePokemona):
    key = ""
    for k,v in pokemoni.items():
        if v['ime'] == imePokemona:
            key = k
            break
    for k,v in pokemoni.items():
        if v['velikost'] < pokemoni[key]['velikost']:
            print(v['ime'])
    

pokemoni = {
    "pokemon1": {"ime": "Pikachu", "tip": "Elektricen", "velikost": 0.4, "teza":6.0},
    "pokemon2": {"ime": "Nijedu", "tip": "Elektricen", "velikost": 0.4, "teza":12.0}
}

manjsiPokemoni(pokemoni, "Pikachu")

n = ['hlapci', 'Jezero']
l = [2018, 2017]

def unija(niz1, niz2):
    n1 = set(list(niz1))
    n2 = set(list(niz2))
    print(n1.union(n2))

unija("macke", "jedim")

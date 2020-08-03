def najmlajsaKnjiga(naslov, leto):
    najmlajsa = ""
    najmlajsaStetje = 0
    for i in range(len(naslov)):
        if leto[i] > najmlajsaStetje:
            najmlajsa = naslov[i]
            najmlajsaStetje = leto[i]
    print(najmlajsa)
    

def unija(niz1, niz2):
    seznam1 = []
    seznam2 = []
    for i in niz1:
        seznam1.append(i)
    for j in niz2:
        seznam2.append(j)
    mnozica1 = set(seznam1)
    mnozica2 = set(seznam2)
    print(mnozica2.union(mnozica1))

unija("macke", "jedim")

def najtezjiPokemon(pokemoni):
    najtezji = ""
    najtezjiStetje = 0
    for vrednost in pokemoni:
        if pokemoni[vrednost]['teza'] > najtezjiStetje:
            najtezji = pokemoni[vrednost]['ime']
            najtezjiStetje = pokemoni[vrednost]['teza']
    print(najtezji)

pokemoni = {
    "pokemon1": {"ime": "Pikachu", "tip": "Elektricen", "velikost": 0.4, "teza":6.0},
    "pokemon2": {"ime": "Nijedu", "tip": "Elektricen", "velikost": 0.4, "teza":12.0}
}

najtezjiPokemon(pokemoni)


def razlika(seznam1, seznam2):
    mnozica1 = set(seznam1)
    mnozica2 = set(seznam2)
    razlikaa = mnozica1.difference(mnozica2)
    print(razlikaa)

def posebniNizi(seznam):
    st = 0
    for i in seznam:
        samoglasnik = False
        for j in i:
            if j in ["a", "e", "i", "o", "u"]:
                samoglasnik = True
                break
        if samoglasnik == False:
            st += 1
    return st


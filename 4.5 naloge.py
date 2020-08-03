"""
def najvisjiDijak(slovar): #definiramo podmetodo najvecji dijak z vhodnim slovarjem
    najvisji = {'ime': None, 'velikost': 0} #definiramo slovar, saj je najlažji način da shranimo ime in velikost
    for i in slovar: #za vsak ključ v slovarju
        if slovar[i]['velikost'] > najvisji['velikost']: #če je velikost dijaka višja kot velikost trenutnega največjega dijaka
            najvisji['ime'] = slovar[i]['ime'] #ime najvisjega dijaka spremenimo na ime dijaka
            najvisji['velikost'] = slovar[i]['velikost'] #velikost najvisjega dijaka nastavimo v slovar
    print('Najvecji dijak/dijakinja je %s in sicer %d cm visok/visoka' %(najvisji['ime'],najvisji['velikost'])) #izpišemo kdo je največji
"""
"""
def najstarejšiDijak(slovar): #definiramo podmetodo najstarejsi dijak z vhodno spremenljivko slovar
    najstarejsi = {'ime': None, 'rojstvo': 5000000}  #definiramo slovar z imenom in neko veliko številko, ki bo leto rojstva vedno manjše
    for s in slovar: #za vsak ključ v slovarju
        if slovar[s]['letoRojstva'] < najstarejsi['rojstvo']: #če je leto rojstva manjše kot rojstvo v slovarju
            najstarejsi['ime'] = slovar[s]['ime'] #nastavimo ime na ime dijaka
            najstarejsi['rojstvo'] = slovar[s]['letoRojstva'] #in leto rojstva na leto dijaka
    print('Najstarejsi dijak/dijakinja je %s in sicer %d let'%(najstarejsi['ime'], 2020-najstarejsi['rojstvo'])) #izpišemo najstarejšega dijaka/dijakinjo in njihovo velikost
"""


def najvisjiDijak(slovar):
    ime = ""
    visina = 0
    for i in slovar:
        if slovar[i]['velikost'] > visina:
            ime = slovar[i]['ime']
            visina = slovar[i]['velikost']
    print(ime, visina)

def najstarejsiDijak(slovar):
    ime = ""
    rojstvo = 999999999999
    for i in slovar:
        if slovar[i]['letoRojstva'] < rojstvo:
            ime = slovar[i]['ime']
            rojstvo = slovar[i]['letoRojstva']
    starost = 2020-rojstvo
    print(ime, starost)


slovar={
    "dijak1":{"ime": "Janez","letoRojstva":1999, "velikost":180},
    "dijak2":{"ime": "Marija","letoRojstva":187, "velikost":167},
    "dijak3":{"ime": "Franci","letoRojstva":2001, "velikost":179},
    "dijak4":{"ime": "Terezija","letoRojstva":2003, "velikost":158}
}

najvisjiDijak(slovar)
najstarejsiDijak(slovar)



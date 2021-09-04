def TOP3stevila(seznam): #definiramo podmetodo top3 stevila
    for i in range(3): #for zanko nastavimo da se ponovi 3x saj moramo dobiti 3 najvecja
        najvecje = max(seznam) #dobimo najvecje stevilo z pomocjo max() fukcije. 
        print(najvecje) #to stevilo izpisemo
        seznam.remove(najvecje) #in ga odstranimo tako da na seznamu imamo naslednje največje stevilo kot najvecje


def obrni(seznam): #definiramo podmetodo obrni z vhodno spremenljivko seznam
    sez = [] #naredimo nov seznam
    for i in range(len(seznam)-1, -1, -1): #naredimo obratno for zanko, ki začne gledati seznam od zadnjega mesta do prvega
        sez.append(seznam[i]) #ta element dodamo na nov seznam
    print(sez) #po končani for zanki izpišemo seznam
    

def najpogostejsaBeseda(seznam): #defirniramo podmetodo najpogostejsa beseda z vhodno spremenljivko v obliki seznama
    slovar = {} #ustvarimo nov slovar
    najpogostejsaBesedaa = "" #naredimo spremenljivko za najpogoistejso besedo
    najpogostejsaStetje = 0 #naredimo se eno spremenljivko, ki bo stela kokrat se beseda ponovi
    for i in seznam: #za vsako besedo na seznamu
        if i not in slovar: #če beseda ni na seznamu
            slovar[i] = 1 #jo damo na seznam
        else: #če je že na seznamu
            slovar[i] += 1 #prištejemo da smo jo še enkrat videli
    for kljuc,vrednost in slovar.items(): #za ključ in vrednost v slovarju
        if vrednost > najpogostejsaStetje: #če se beseda ponovi večkrat kot najbolj ponovljena številka
            najpogostejsaBesedaa = kljuc #nastavimo da je najbolj pogosta beseda
            najpogostejsaStetje = vrednost #pa shranimo kolikokrat se ponovi
    
def statistika(seznam): #definiramo podmetodo statistika z vhodno spremenljivko v obliki seznama
    slovar = {} #ustvarimo nov slovar
    for i in seznam: #za vsak element v seznamu
        if i not in slovar:
            slovar[i] = "*"
        else:
            slovar[i] += "*"
    for i in range(1,6):
        print(i + ": " + slovar[i])
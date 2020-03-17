

def TOP3stevila(seznam): #definiramo podmetodo TOP3Stevila z vhodno spremenljivko seznam
    l = [] #naredimo prazen seznam na katerega bomo shranili naša števila
    while len(l) != 3: #dokler nimamo top3 stecvila bo zanka delovala
        l.append(max(seznam)) #zanka pripne največje št iz vhodnega seznama na l
        seznam.remove(max(seznam)) #odstranimo največji element iz seznama
    print(l)#izpišemo top3 števila


def obrni(seznam): #definiramo podmetodo obrni z vhodom seznama 
    print([seznam[i] for i in range(len(seznam)-1,-1, -1)]) #izpišemo enovrstično for zanko ki nam obrne niz



def kolikoElementov(seznam): #definiramo podmetodo kolikoElementov z vhodom seznama
    l = [] #naredimo prazen seznam
    for items in seznam: #za vsak element v seznamu
        if items not in l: #če ni na praznem seznamu 
            l.append(items) #priprnemo na seznam z tem lahko podvojene elemente odstranimo saj če je podvojen se nebo appendalo
    print(len(l)) #ipišemo dolžino nepodvojenega seznama



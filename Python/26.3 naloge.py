def razlicniZnaki(poljubnoDolgoBesedilo): #definiramo podmetodo razlicniZnaki z vhodom poljubnoDolgoBesedilo
    dic = {} #definiramo slovar
    for crke in poljubnoDolgoBesedilo: #za vsak znak v besedilu
        if crke!=" ": #če ni presledek
            if crke not in dic: #če ni v slovarju
                dic[crke] = 1 #nastavi vrednost na 1
    print(len(dic)) #izšiši koliko elementov je v slovarju


def najpogostejseStevilo(seznamStevil): #defirniarmo podpogram najpogostejseŠtevilo z vhodnim seznamom
    dic = {} #definiramo seznam
    for items in seznamStevil: #za vsak element v seznamu
        if items not in dic: #če ni v slovarju
            dic[items] = 1 #nastavimo vrednost ključa na 1
        else: #če je 
            dic[items] += 1 #povečamo vrednost ključa za 1
    maximum = max(dic, key=dic.get) #dovbimo maximalno vrednost ključa
    print(maximum) #izpišemo ta ključ
    
def redkiZnaki(poljubnoDolgoBesedilo): #definiramo redkiZnaki z vhodnim besedilom
    dic = {} #definiramo nov slovar
    for items in poljubnoDolgoBesedilo: #za vsak element v besedliu
        if items not in dic: #če ni v seznamu
            dic[items] = 1 #nastavimo ključ na 1
        else: #če je 
            dic[items] += 1 #povečamo vrednost za 1
    [print(key) for key,val in dic.items() if val==1] #gremo čez vsak ključ in ga izpišemo če je vrednost 1


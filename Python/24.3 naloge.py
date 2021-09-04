def prastevila(sez): #definiramo podmetodo praštevila
    l = [] #anredimo prazen seznam
    for items in sez: #za vsako stvar v vhodnem seznamu
        if items>1: #če je večje kot 1
            for i in range(2, items): #za vsako število od 2 do samega števila
                if items%i==0: #če je deljivo 
                    break #končaj zanko
            else: #če ni deljivo z nobeno 
                l.append(items) #jo daj na seznam
    print(l) #ispis seznama
 
def najpogostejseStevilo(sez): #definiramo podmetodo najpogostejeStevilo z seznamom kot vhod
    dic = {} #definiramo praznen slovar
    for items in sez: #za vsako stvar na seznamuj
        if items not in dic: #če ni v slovarju 
            dic[items] = 1 #nastavimo ključ vrednosti na 1
        else: #če je
            dic[items] += 1 #prištejemo 1
    maximum = max(dic, key=dic.get) #dobimo najbolj pogosto črko v seznamu
    print(maximum) #in jo izpišemo

def najpogostejsaBeseda(besedilo):
    besedilo = besedilo.split()
    dic = {} #definiramo praznen slovar
    for items in besedilo: #za vsako stvar na seznamuj
        if items not in dic: #če ni v slovarju 
            dic[items] = 1 #nastavimo ključ vrednosti na 1
        else: #če je
            dic[items] += 1 #prištejemo 1
    maximum = max(dic, key=dic.get) #dobimo najbolj pogosto črko v seznamu
    print(maximum) #in jo izpišemo

def najpogostejsoStevko(sez): #definiramo podmetodo najpogostejsoStevko z seznamom kot vhod
    sez = [str(i) for i in sez] #spremenimo vsak element v niz
    sez = "".join(sez) #seznam pretvorimo v en dolg niz
    dic = {} #definiramo prazen slovar
    for i in sez: #za vsao števko v nizu
        if i not in dic: #če ni v slovarju
            dic[i] = 1 #nastavimo ključ na 1
        else: #če je 
            dic[i] += 1 #prištejemo 1
    maximum = max(dic, key=dic.get) #dobimo maksimalno vrednost
    print(maximum) #izpišemo maksimalno vrednost


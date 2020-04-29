import re #importamo knjiznico re

def razlicneBesede(niz): #definiramo podmetodo razlicne besede z vhodnim nizom
    niz = niz.lower() #pretvorimo v male crke
    niz = re.split(', |_|-|!| ', niz) #razdvojimo niz v seznam besed
    dic = {} #ustvarimo slovar
    for items in niz: #za vsak element v seznamu
        if items not in dic: #če ni v slovarju
            dic[items] = 1 #dodamo v slovar
        else: #drugače če je 
            dic[items] += 1 #prištejemo kolikokrat se pojavi
    [print(k, v) for k,v in dic.items()] #izpisemo vsako besedo in kolikorkrat se pojavi
    

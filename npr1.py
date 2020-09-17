
def zapisiPrastevilaDo100(): #definiramo metodo
    datoteka = open("pravljica.txt", "w") #odpremo datoteko v načinu branja
    for i in range(100): #naredimo for zanko do št 100
        if i>1: #pogledamo če je št večje kot ena saj je ena deljivo z vsakim številom
            for j in range(2,i): #če ni deljivo gremo skozi for znako, ki preveri ali je še kakšen deljitelj poleg 1
                if i%j == 0: #če je še kakšen delitelj 
                    break #končamo zanko
            else: #će ni nobenega delitelja 
                datoteka.write("%s\n" %i) #zapišemo št
    datoteka.close() #po zapisanem zapremo datoteko

def prestejEnke(): #definiramo podmetodo 
    datoteka = open("binarni_zapis.txt", "r") #odpremo datoteko "binarni zapis.txt" v načinu za branje
    c = datoteka.read() #preberemo datoteko
    s = 0 #usvarimo spremenljivko ki bo štela
    for i in c: #gremo skozi vsak niz v datoteki
        if "0" in i: #če je ničla
            s += 1 #jo prištejemo
    datoteka.close() #zapremo datoteko ko smo končali z njo
    return s #in vrnemo kolikokrat se ponovi število 0

def prestejBla(): #definiramo podmetodo
    datoteka = open("pravljica.txt", "r") #odpremo datoteko v načinu branja
    c = datoteka.read() #preberemo datoteko 
    s = 0 #naredimo spremenljivko z katero bomo šteli
    c.split(" ") #razdeljimo en velik niz na seznam besed
    for i in c:       #gremo skozi vsako besedo  
        if "bla" in i:#če se v besedi pojavi bla
            s += 1 #prištejemo 1
    datoteka.close() #ko smo končali z datoteko jo zapremo
    return s #in vrnemo kolikokrat se ponovi "bla" v datoteki

def zamenjajDatoteki(dat1, dat2): #definiramo podmetodo
    d1 = open(dat1, "r") #odpremo datoteko 1
    d1r = d1.read() #jo preberemo
    d2 = open(dat2, "r") #odpremo datoteko2
    d2r = d2.read() #jo preberemo

    d1.close() #ko preberemo lahko zapremo
    d2.close() #ko preberemo lahko zapremo
  
    d1c = open(dat1, "w") #zopet odpremo datoteke v načinu zapisa
    d1c.write(d2r) #in zapišemo vse kar je bilo na drugi datoteki
    d2c = open(dat2, "w") #odpremo še drugo datoteko
    d2c.write(d1r) #in zapišemo vse kar je bilo na prvi datoteki

    d1c.close() #zapremo datoteke
    d2c.close() #zapremo datoteke

def obrniZapis(datoteka): #definiramo novo metodo
    f = open(datoteka, "r") #odpremo datoteko v načinu za branje
    fc = f.read() #preberemo datoteko
    f.close() #in jo zapremo ko končamo z njo
    f = open(datoteka, "w") #zopet jo odpremo v načinu za zapis
    f.write(fc[::-1]) #zapišemo obrnjeno
    f.close() #zapremo datoteko zopet


    
    

import random
def najpogostejseStevilo(polje): #definiramo podmetodo najpogostejse stevilo z vhodno spremenljivko polje
    slovar = {} #uzpostavimo slovar
    for i in polje: #naredimo for zanko, ki bo pregledala vhodno spremenljivko oz. polje
        if i not in slovar: #pogledamo, če je iti elemenet polja v slovarju
            slovar[i] = 1 #če ni ga dodamo v slovar
        else: #v obratnem primeru
            slovar[i] += 1 #prištejemo vrednost 1 k obstajajoči vrednost
    print(max(slovar, key=slovar.get)) #izpišemo max vrednost v slovarju
    print(slovar[max(slovar, key=slovar.get)]) #ter kolikokrat se je ta številka pojavila


l = []
for i in range(1000):
    l.append(random.randint(1,100))


def pretvoriv2(a):
    trenutna = a
    string = ""
    while trenutna != 1:
        string += str(trenutna%2)
        trenutna = trenutna // 2
    string += "1"
    print(string[::-1])

pretvoriv2(0)

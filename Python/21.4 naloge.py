import re #importamo knjiznico re

def razlicneB2esede(niz): #definiramo podmetodo razlicne besede z vhodnim nizom
    niz = niz.lower() #pretvorimo v male crke
    niz = re.split(', |_|-|!| ', niz) #razdvojimo niz v seznam besed
    dic = {} #ustvarimo slovar
    for items in niz: #za vsak element v seznamu
        if items not in dic: #če ni v slovarju
            dic[items] = 1 #dodamo v slovar
        else: #drugače če je 
            dic[items] += 1 #prištejemo kolikokrat se pojavi
    [print(k, v) for k,v in dic.items()] #izpisemo vsako besedo in kolikorkrat se pojavi
    
def razlicneBesede(niz):
    niz = niz.split()
    for i in niz:
        i = i.lower()
    slovar = {}
    for i in niz :
        if i not in slovar:
            slovar[i] = 1
        else:
            slovar[i] += 1
    for i in slovar:
        print(i, slovar[i])

def numerologija(niz): #definiramo podmetodo numerologija z vhodno spemenljivko niz
	stetje = 0#ustvarimo spremenljivko z katero bomo računali
	for i in niz: #gremo čez vsako črko v nizu
		if i in ["a", "i", "j", "q", "y"]: #če je v tej skupini
			stetje += 1 #prištejemo 1 in tako dalje
		elif i in ["b", "k", "r"]:  
			stetje += 2
		elif i in ["c", "g", "l", "s"]:
			stetje += 3
		elif i in ["d", "m", "t"]:
			stetje += 4
		elif i in ["e", "h", "n", "x"]:
			stetje += 5
		elif i in ["u", "v", "w"]:
			stetje += 6
		elif i in ["z", "o"]:
			stejte += 7
		elif i in ["f", "p"]:
			stejte += 8
	novoSt = int(str(stetje)[0]) + int(str(stetje)[1]) #seštejemo prvo števko in zadnjo števko torej če imamo 12 seštejemo 1 + 2 da dobimo 3
	print(novoSt) #in izpišemo to številko
 
def mankajocaStevila(besedilo): #definiramo metodo mankajoca Stevila z vhodno spremenljivko besedilo
	besedilo = besedilo.split("-") #besedilo razdelimo na seznam z samimi črkami
	najvecjeSt = besedilo[-1] #vzamemo največjo, ki je zadnja
	najmanjseSt = besedilo[0] #vzamemo najmanjšo, ki je prva
	for i in range(int(najmanjseSt), int(najvecjeSt)+1): #od najmanjse do najvecje cifre gremo
		if str(i) not in besedilo: #pogledamo ali je ni v seznamu
			print("(" + str(i) + ")")  #če je ni izpišemo jo z oklepajom
		else: #če je v seznamu
			print(i) #jo normalno izpišemo
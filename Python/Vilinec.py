class Vilinec: #definiramo razred Vilinec
    def __init__(self, ime:str, emsv:int, spol:str, imeOceta:str): #naredimo constructor metodo, ki sprejme ime kot niz, emsv kot int, spol kot str in ime oceta kot str
        self.ime = ime 
        self.emsv = emsv
        self.spol = spol
        self.imeOceta = imeOceta 

    def __str__(self): #definirma metodo, ki vrne vrednost ko se shrani
        return '%s;%d;%s;%s' %(self.ime, self.emsv, self.spol, self.imeOceta) #vrnemo niz v formatu ime;emsv;spol;imeOceta

    __repr__ = __str__ #__repr__ pove, da ko se objekt shrani v seznam, da se pokaže kot __str__ in ne mesto objekta na pomnilniku
 
    def imeInPriimek(self): #definiramo podmetodo ime in priimek
        if self.spol.lower() == 'm': #če je spol moški
            p = 'sin' #damo pridevnik sin
        else: #drugače 
            p = 'hči' #dodamo hčerko

        return self.ime + ', ' + p + ' ' + self.imeOceta #vrnemo v formatu ime , pridevnik Imeoceta

    def preveriEMSV(self): #definiramo podmetoido preveriEMSV
        s = 0 #ustvarimo metodo, na katero bomo seštevali
        for i in str(self.emsv)[:8]: #gremo skozi prvih 8 števk v emsv
            s += int(i) #in jih prištejemo
        if s%10 == int(str(self.emsv)[-1]): #nato pogledamo, če je ostanek deljenja z 10 enak kot zadnja št
            return 'Veljaven' #vrnemo veljaven
        else: #drugače 
            return 'Neveljaven' #Ni veljaven

def vnosVilincev(n): #definiramo metodo vnosVilincev
    l = [] #ustvarimo seznam
    while len(l) != n: #ustvarimo while znako dokler se seznam ne napolni z toliko vilincev kolikor hočemo
        ime = input('Vnesite ime: ') #Vnesemo vse vrednosti, ki jih potrebujmo
        emsv = int(input('Vnesite št: '))
        spol = input('Vnesite spol (M ali F): ')
        imeOceta = input('Vnesite ime oceta: ')
        l.append(Vilinec(ime = ime, emsv = emsv, spol = spol, imeOceta = imeOceta)) #ter dodamo na seznam ustvarjenega vilinca

    return l #vrnemo ta seznam


def shraniVilince(seznamVilincov): #definiramo podmetodo shraniVilince, z vhodno spremenljivko seznamVilincov
    dat = open('shranjeniVilinci.txt', 'a') #odpremo, datoteko v načinu append, kar pomeni, da dodaje vedno na konec
    for i in seznamVilincov: #za vsakega vilinca na seznamu
        dat.write(str(i) + '\n') #ga zapišemo in pojdemo v novo vrsto
    dat.close() #ter datoteko zapremo, da ne porabimo pomnilnik



def sestejStevke(cifra):
	if len(str(cifra)) == 0:
		return 0
	else:
		if int(str(cifra)[0])%2==0:
			return 1 + sestejStevke(int(str(cifra)[1:]))
		elif int(str(cifra)[0])%2==1:
			return 0 + sestejStevke(int(str(cifra)[1:]))

print(sestejStevke(1233322))

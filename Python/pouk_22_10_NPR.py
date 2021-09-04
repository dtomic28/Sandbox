def metoda1(st): #definiramo podmetodo 
    if st == 1: #naredimo robni stavek, ki ustavi rekurzijo ko je st = 1
        return 1 #vrnemo 1
    else: #če nismo prišli do robnega stavka
        return str(metoda1(st//2)) + str(st%2) #združimo niz celoštevilskega deljenja z 2 z ostankom od deljenja stevila z dve npr "01110" + "1"

st = 1 #nastavimo stevilo na 1
def metoda2(st1, st2): #definiramo metodo z dvemi spremenljivkavi
    global st #spremenljivko st nastavimo na globalno, kar pomeni, da jo lahko uporabljamo znotraj metode, četudi ni v metodi
    if st%st1 == 0 and st%st2 == 0: #če je št deljivo z obema številoma
        return st #se vrne število
    else: #če ne 
        st += 1 #število povečjamo na 1
        metoda2(st1,st2) #kličemo rekurzijo z istimi števili
        return st #vrnemo število, ko se rekurzija zaključi
 
def metoda3(n): #definiramo metodo z vhodno spremenljivko n
    if n == 1: #če je št enako 1 
        return 1 #zaključimo rekurzijo in vrnemo 1
    else: #če ni še robni pogoj
        return 3*metoda3(n-1) + 2 #potrojimo št, ki dobimo iz rekurzivne metode in ji prištejemo 2

def metoda4(niz, znak): #definiramo podmetodo z dvema spremenljivkama niz in znak
    if niz == "": #če je niz prazen
        return 0 #vnremo št 0 in zaključimo poglobitev rekurzije
    else: #če ni še robni pogoj
        if niz[0] == znak: #če je prvi znak niza enak znaku
            return 1 + metoda4(niz[1:], znak) #vrnemo št 1 in kličemo rekurzijo naprej
        else: #če ni znak 
            return 0 + metoda4(niz[1:], znak)#vrnemo 0 in kličemo rekurzijo
    
def metoda5(niz): #definiramo metodo z vhodno spremenljivko niz
    if len(niz) == 1: #če je dolžina niza enaka 1
        return niz #vnremo niz
    else: #če še ni robni pogoj dosežen
        if niz[0] == niz[1]: #če sta znaka podvojena
            return "" + metoda5(niz[1:]) #vrnemo prazen niz in kličemo metodo naprej z nizom brez prvega znaka
        else: #će ne
            return niz[0] + metoda5(niz[1:]) #vrnemo prvi znak niza in kličemo rekurizjo na krajši niz za en znak

def forr(n,st=0):
    if st == n:
        return
    else:
        print(st)
        forr(n, st+1)

print(metoda3(4))

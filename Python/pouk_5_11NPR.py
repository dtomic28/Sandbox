def aliJePravilen(niz, c=0): #definiramo podmetodo ali je pravilen z vhodno spremenljivko niz in spremenljivko c ki bo stela koliko je enic
    if len(niz) == 1: #Nastavimo robni stavek, ki pogleda če je samo en znak
        if niz == "1": #če je pogledamo če je enica
            c += 1 #če je prištejemo 1
        if c%2==1 and niz == "0" or c%2==0 and niz == "1": #pogledamo če je bit pravilen
            return True #vrnemo true če je 
        else: #v obratnem primeru
            return False #vrnemo da je false
    else: #če ni še robni stavek
        if niz[0] == "1": #pogledamo, če je prvi znak niza 1
            c += 1 #če je prištejemo 1
        return aliJePravilen(niz[1:], c = c) #pokličemo rekurzijo naprej
        
def cifer(text,znak): #definiramo podmetodo cifer z vhodno spremenljivko teksta in znak, z katerim bomo zamaknili cesarjevo šifro
    s = (ord(znak)- 96) #določimoo zaporedje črke, ki je bila vnešena
    if len(text) == 0: #če je robni pogoj dosežen
        return "" #vrnemo prazen niz
    else: #v obratnem primeru
        return chr((ord(text[0]) + s - 97) % 26 + 97) + cifer(text[1:],znak) #vrnemo prvi znak niza zamakjen za s in pokličemo rekurzijo


def obrni(niz):
    if len(niz) == 0:
        return ""
    else:
        return obrni(niz[1:]) + niz[0]

print(obrni("Danijel"))
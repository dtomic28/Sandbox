vnos = input("Vnesite niz: ")


def crke(niz):
  for i in range(len(niz)-1,-1,-1): #pregleda vsako stevilko od dolzine niza-1 do nevključno -1 in vsakič odštejemo 1
    array = niz[i]  #spremenljivko array nastavimo na crko glede na stetje v zanki
    print(array) #ispis te crke

crke(vnos)



def obrni(niz):
  vsota = "" #nastavimo prazno spremenljivko na katero bomo shranjevali niz
  for i in range(len(niz)-1,-1,-1): #pregleda vsako stevilko od dolzine niza-1 do nevključno -1 in vsakič odštejemo 1
    vsota += niz[i] #doda crko na spremenjlivko
  print(vsota) #izpise spremenljivko

obrni(vnos)



def sodoCrke(niz):
  vsota = "" #nastavimo prazno spremenljivko
  for i in range(len(niz)): #pregleda vsako stevilko od dolzine niza-1 do nevključno -1 in vsakič odštejemo 1
    if i%2==0: #če je mesto črke sodo 
      vsota += niz[i] #bomo dodali črko v niz
  print(vsota) #ispis niza

sodoCrke(vnos)



def najpogostejsaCrka(niz):
  crke = [] #naredimo prazen seznam
  for i in range(len(niz)): #za pozicijo črke na seznamu
    nizi = niz[i] #shranimo črko na spremenljivko
    crke.append(nizi) #črko dodamo na seznam
  
  ponavljajoce = [] #naredimo prazen seznam za shranjevanje ponavljajočih črk
  for x in range(len(crke)): #za vsako pozicijsko številko črke v nizu
    stetje = 0 #spremenljivko stetje nastavimo na 0
    for j in range(x+1,len(crke)): #za vsako pozicijsko črke v nizu brez prejšnje črke
      if crke[x]==crke[j]: #če je prva nevključena črka ponovljena
        stetje += 1 #štetju prištejemo 1
        ponavljajoce.append([crke[x],stetje]) #na seznam ponavljajoče napišemo katera črka se je ponovila in kolikokrat
  for el in range(len(ponavljajoce)): #za vsako pozicijo na seznamu ponavljajoce
    for els in range(len(ponavljajoce)-1,el,-1): #za vsako pozicijo na seznamu ponavljajoce ampak stejemo od zadnje
      if ponavljajoce[el][1]>=ponavljajoce[els][1]: #če se bodo ponovile črke večkrat 
        print(ponavljajoce[el][0]) #jo izpišemo
    
najpogostejsaCrka(vnos)

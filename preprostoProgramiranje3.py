vnos = int(input("Vnesite stevilo x: "))

def lumos(n): #definiramo podpogram lumnos z vhodno spremljivko n
    vsota = 0 #spremenljivko vsota nastavimo na 0
    for i in range(1, n): #za vsako stevilo v razponu od ena do nevključno vhodne štetivle
        if n%i==0: #če je število v delitelj od vhodnme spremenljivko
            vsota += i #prištejemo delitelja na vsoto
    
    if vsota == n: #če je vsota deliteljev enaka vhodnemu stevilu
        print("stevilo je popolno st") #je popolno stevilo
    else: #če ne
        print("stevilo ni popolno") #število ni popolno

lumos(vnos)
        
    
def GringottsBanka(vsota): #definiraj podpogram Gringotts bank z vhodno spremenljivko vsota
    bankovci = [500,200,100,50,20,10,5,2,1] #bankovci ki so na voljo

    for i in range(len(bankovci)): #za vsako stevilko v razponu od 1 do koliko moznosti imamo za bankovce
        stetje = 0 #stetje je enako 0
        while vsota>=bankovci[i]: #dokler je vsota večja kot bankovec
            vsota -= bankovci[i] #bankovec oštej
            stetje += 1 #prištej ena na števec zato da vidimo kolikokrat smo dobili kateri bankovec
        if stetje > 0: #če je stetje vecje kot 0 kar pomeni če dobimo nek bankovec
            print(str(stetje) + " x", bankovci[i]) #ga izpišemo
        
GringottsBanka(vnos)
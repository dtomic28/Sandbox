import sys

def zracunajOdvrzeno(praznovanje):
    w,d = 0,0.5
    for i in praznovanje:
        if(i == "S"):
            w += (1*d)
        d = d*0.5
    return w
    
def sestevanjeUlomkov():
    vnos = input("Vnesite r in n")
    r,n = int(vnos[0]),int(vnos[-1])
    arr = []
    c = 0
    for i in range(r):
        vnos = input("Vnesite praznovanje")
        c += zracunajOdvrzeno(vnos)
    print(round(c))

""" 



"""

def aliSeUjema(seznam, beseda):
    for i in seznam:
        if(beseda[i[1]] != i[0]):
            return False
    return(True)

def preveriVzorec(sez, vzorec):
    arr = []
    for i in range(len(vzorec)):
        if(vzorec[i] != "*"):
            arr.append([vzorec[i], i])
    for i in seznam:
        if(len(i) == len(vzorec)):
            if(aliSeUjema(arr, i)==True):
                print(i)
""" 








"""
#preverimo katera vrstica ima največ števil med dvema ničlama na začetku in koncu
def preveriVX(x,sez):
    c = 0
    sez = []
    z,k = 0
    for index,i in enumerate(sez[x]):
        if i!=c:
            c+=i
        else:
            sez.append([c,z,k])
            c = 0
            z = k
            k = index-1
    return max(sez)
    
def vertikalnoToHorizontalo(sez,y):
    arr = []
    for i in sez:
        arr.append(i[y])
    return arr

#Preverimo kateri stolpec ima največjo vsoto med dvema ničlama
def preveriVY(y,sez):
    arr = vertikalnoToHorizontalo(sez, y)
    c = 0
    sez = []
    z,k = 0
    for index,i in enumerate(arr):
        if i!=c:
            c+=i
        else:
            sez.append([c,z,k])
            c = 0
            z = k
            k = index-1
    return max(sez)

def preveriCeliY(sez):
    arr = []
    for i in range(len(seznam[0])):
        arr.append(preveriVY(i,sez))
    return max(arr)

def preveriCeliX(sez):
    arr=[]
    for i in range(len(seznam)):
        arr.append(preveriVX(i,sez))
    return max(arr)

#Združimo vrednost ter najdemo koordinato
def preveriGenialno(seznam):
    x = preveriCeliX(seznam)
    y = preveriCeliY(seznam)
    xV = (x[1] + x[2])//2
    yV = (y[1] + y[2])//2
    print("x: " + xV + " " + "y: " + yV + " " "=" + (x[0] + y[0]))


#Naloga, deluje tako, da najde najboljše zaporedje števil med dvema ničlama oz. koncoma to naredi vertikalno in horizontalno. Program najde optimalno koordinato, tako da 
#najde sredinsko vrednost v tem zaporedju za obe koordinate in najde točko. Program prejeme seznam v seznamu torej [[][][]]

"""

"""
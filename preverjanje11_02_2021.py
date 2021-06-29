def rekurzijaMini(n):
    if n==0:
        return ""
    else:
        vrstica = ""
        for i in range(n):
            vrstica += "*"
            print(vrstica)
            

def rekurzija(n):
    if n==0:
        return ""
    else:
        rekurzija(n-1)
        rekurzijaMini(n)
        
    
rekurzija(4)

"""
 def rekurzija(n):
    if n==0:
        return 1
    else:
        return 4*rekurzija(n-1)

print(rekurzija(2))
 
 def ozdravitev(self,napoj):
    self.zivljenskeTocke += napoj

   
 
def vrniZapStevilo(zap):
    s = 0
    zap = zap[::-1]
    for i in range(len(zap)):
        s += int(zap[i]) * 3**i
    return s 

print(vrniZapStevilo("122"))


def preveriZapStevila(zap):
    if len(zap) == 0:
        return True
    else:
        if int(zap[0]) >= 3:
            return False
        else:
            return preveriZapStevila(zap[1:])

print(preveriZapStevila("122"))

"""
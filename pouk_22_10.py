def metoda1(st):
    if st == 1:
        return 1
    else:
        return str(metoda1(st//2)) + str(st%2)

def metoda2(st1, st2):
    st = min([st1, st2])
    while True:
        if st % st1 == 0 and st % st2 == 0:
            print(st)
            break
        else:
            st += 1

def metoda3(n):
    if n == 1:
        return 1
    else:
        return 4*metoda3(n-1) + 1

def metoda4(niz, znak):
    if niz == "":
        return 0
    else:
        if niz[0] == znak:
            return 1 + metoda4(niz[1:], znak)
        else:
            return 0 + metoda4(niz[1:], znak)
    
print(metoda4("ananas", "n"))

def odpraviNapake(niz):
    

        
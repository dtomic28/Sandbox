
def preveriEmso():
    vnos = input("Vnesite emso: ")
    vsota = 0
    faktor = 7
    for i in range(0, len(vnos)-1):
        vsota += int(vnos[i])*faktor
        faktor -= 1
        if faktor==1:
            faktor =7
    zadnjaStevka = int(vnos[len(vnos)-1])
    if (vsota + zadnjaStevka)%11==0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(preveriEmso())

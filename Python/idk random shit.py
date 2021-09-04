

def kvadrat(n):
    for x in range(n):
        vrstica = ""
        for y in range(n):
            if x<n//2:
                vrstica += "P "
            else:
                vrstica += "n "
        print(vrstica)


kvadrat(4)
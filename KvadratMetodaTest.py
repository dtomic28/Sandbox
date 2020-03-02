#hello this is a test

def kvadrat(vnos):
    for i in range(vnos):
        vrstica = ""
        for j in range(vnos):
            if i==j:
                vrstica += "1 "
            else:
                vrstica += "0 "
        print(vrstica)


if __name__ == "__main__":
    N = int(input("Vnesite st: "))
    kvadrat(N)
    print("This is it huh?")




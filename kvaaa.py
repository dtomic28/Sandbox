iw = "odinwaoindwa"

for i in range(len(iw)):
    vrstica = ""
    for j in range(len(iw)):
        if i>=j:
            vrstica += "1 "
        else:
            vrstica += "0 "
    print(vrstica)


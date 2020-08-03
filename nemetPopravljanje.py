vnos = input('vnesite')
niz = ""
for crke in vnos:
    niz = crke + niz
for i in range(len(niz)):
    v = ""
    for j in range(len(niz)):
        if i==j or i+j==len(niz)-1:
            v += niz[i] + " "
        else:
            v += "- "
    print(v)




def odstraniPodvojeneZnake(besedilo):
    niz = ""
    bes = ""
    for i in besedilo:
        niz += i
        if len(niz)==3 and len(set(niz))==1:
            bes += niz[0]
            niz = ""
        elif len(niz)==3 and len(set(niz))!=1:
            bes += niz
            niz = ""
    print(bes)

odstraniPodvojeneZnake("ana")

def kvadrat(niz):
    niz = niz[::-1]
    for i in range(len(niz)):
        vrstica = ""
        for j in range(len(niz)):
            if i==j or i+j==len(niz)-1:
                vrstica += niz[i] + " "
            else:
                vrstica += "- "
        print(vrstica)

kvadrat("anja")



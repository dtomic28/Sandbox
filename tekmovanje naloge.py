
def fakulteta(n):
    vsota = 1
    for i in range(1, n+1):
        vsota = vsota * i
    print(vsota)


def vsotaSodihDoN(n):
    vsota = 0
    for i in range(1, n):
        if i%2==0:
            vsota += i
    print(vsota)

def vsotaPrvihNSodih(n):
    stetje = 0
    vsota = 0
    st = 2
    while stetje!=n:
        vsota += st
        st += 2
        stetje += 1
    print(vsota)

vsotaPrvihNSodih(5)
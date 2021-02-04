def hokusPokus(N,i):
    if(N==0):
        return
    else:
        print('0'*(N)+'1'*(i-N))
        hokusPokus(N-1, i)

def notranja(st,j,i):
    if j == st:
        return ""
    else:
        if i+j == st-1 or i==j or st//2 == i or st//2 == j:
            return "1 " + notranja(st,j+1,i)
        else:
            return "0 " + notranja(st,j+1,i)

def zunanja(st, i=0):
    if i >= st:
        return
    else:
        j = 0
        print(notranja(st, j, i))
        return zunanja(st, i+1)


def rekurzija2(n,m):
    if (m==0):
        return ""
    else:
        if n==m :
            return rekurzija2(n, m-1) + "1"
        else:
            return rekurzija2(n, m-1) + "0"

def rekurzija1(n,m):
    if (n==0):
        return
    else:
        rekurzija1(n-1,m)
        print(rekurzija2(n,m))


rekurzija1(4,4)
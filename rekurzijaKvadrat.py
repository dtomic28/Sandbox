st = 4

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

zunanja(9)

"""
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1


"""
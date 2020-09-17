def pretvoriVBinarno(st):
    n = ""
    while True:
        if st==0:
            n += "0"
            break
        n += str(int(st)%2)
        st = st//2
    if len(n) != 8:
        n = ((8-len(n)) * "0") + n  
    return n 


def dvaKa(st):
    n = ""
    for i in st:
        if i == "0":
            n+= "1"
        else:
            n += "0"
    return(bin(int(n,2) + int("1",2))[2:])

def deDvaKa(st):
    st = bin(int(st,2) - int("1", 2))[2:]
    n = ""
    for i in st:
        if i == "0":
            n += "1"
        else:
            n += "0"
    return n

def binAdd(s1, s2):

    n = ''
    pristejemo = 0

    najvecja = max(s1, s2)

    s1B = (bin(int(str(s1), 2)))[2:]
    s2B = (bin(int(str(s2), 2)))[2:]

    s2B = dvaKa(s2B)
    

    i = 8 - 1
    while(i >= 0):
        s = int(s1B[i]) + int(s2B[i])
        if s == 2: #1+1
            if pristejemo == 0:
                pristejemo = 1
                n += "0"
            else:
                n += "1"
        elif s == 1: # 1+0
            if pristejemo == 1:
                n += "0"
            else:
                n += "1"
        else: # 0+0
            if pristejemo == 1:
                n += "1"
                pristejemo = 0   
            else:
                n += "0"

        i = i - 1

    if pristejemo>0:
        n += "1"
    return deDvaKa(n[::-1])

print(binAdd(144,100))
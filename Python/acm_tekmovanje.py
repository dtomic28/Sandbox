""" def izenaceno(s):
    dic = {}
    sett = set()
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            sett.add(i)
    if sett != {'x', 'o'} or dic["x"] != dic["o"]:
        return False
    
    print(dic)
    print(s) """
    
def izenaceno(s):
    dic = {}
    se = set()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
            se.add(s[i])
    if se != {'x', 'o'} or dic["x"] != dic["o"]:
        return False
    for i in range(0,len(s),3):
        if len(set(s[i:i+3]))==1 and len(s[i:i+3]) == 3:
            return False
    return True
    
def findZ(z,sez):
    for i in range(len(sez)):
        if sez[i][0] == z:
            return i
    else:
        return None

def metoda(n,z,sez):
    i = findZ(z,sez)
    while True:
        i = findZ(z,sez)
        if i == None:
            return z
        z = sez[i][1]
    
print(metoda(6,1,[[1,2],[2,4],[3,1],[6,5]]))


    


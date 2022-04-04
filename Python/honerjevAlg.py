sezSt=[3,5,-7,-9,4,4]
sezDel=[]
for i in range(1,abs(sezSt[-1])+1,1):
    if(sezSt[-1]%i==0):
        sezDel.append(i)
r=len(sezDel)
for i in range(r):
    sezDel.append(sezDel[i]/sezSt[0])
r=len(sezDel)
for i in range(r):
    sezDel.append(-sezDel[i])
sezDel=set(sezDel)
sezDel=list(sezDel)
numbersSez=[]
while(len(sezSt)!=1):
    for i in sezDel:
        fakeSez=list(sezSt)
        timer=1
        fakeString=["  "]
        for j in fakeSez:
            n=i*j
            fakeString.append(" "+str(n))
            if(timer<len(sezSt)):
                fakeSez[timer]=sezSt[timer]+n
            timer+=1
        if(fakeSez[-1]==0):
            printString="   | "
            for fake in sezSt:
                printString+=str(fake)+" "
            printString2="   | "
            for fake in fakeString:
                printString2+=str(fake)
            print(printString)
            print(printString2)
            print("---|-----------------")
            printString3=str(i)+" |"
            for fake in fakeSez:
                printString3+=" "+str(fake)
            print(printString3)
            numbersSez.append(i)
            fakeSez.pop(-1)
            sezSt=list(fakeSez)
print(numbersSez)
def bubbleSort(sez): 
    n = len(sez) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if sez[j] > sez[j+1] : 
                sez[j], sez[j+1] = sez[j+1], sez[j] 

gace = ["c","b","a"]
bubbleSort(gace)
print(gace)
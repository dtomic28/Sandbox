def rekurzija(int):
    if int==1:
        return 1
    else:
        int * rekurzija(int-1)
    

print(rekurzija(5))
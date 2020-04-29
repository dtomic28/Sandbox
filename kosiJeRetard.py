def razlicneBesede():
    i="Avtomobilom se vozimo po cesti. Avtomobilom se lahko vozimo trezni."
    slovar={}
    vsota=0
    i=i.replace("."," ")
    i=i.replace(","," ")
    i=i.replace("!"," ")
    i=i.replace("?"," ")
    i = i.split()
    for j in i:
        if (j not in slovar):
            slovar[j] = 1
        else:
            slovar[j]+= 1
    print(slovar)
razlicneBesede()
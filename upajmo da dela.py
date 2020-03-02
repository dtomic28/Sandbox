def funkcija(niz1,niz2):
    stetje = 0
    novniz = ""
    karakterji = 0
    while karakterji!=len(niz2):
        for crke in niz2:
            if crke==niz1[stetje]:
                novniz += crke
                if stetje!=len(niz1)-1:
                    stetje += 1
                else:
                    niz1 = "*" * len(niz1)
            else:
                novniz += "-"
            karakterji += 1    
    print(novniz)

funkcija("dol z vlado","še dobro, da lahko z volitvami vplivamo na dobrobit naroda")

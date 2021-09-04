def klobukIzbiruh():
    vnos = int(input("Vnesite st: "))
    stetje = 0
    for i in str(vnos):
        stetje += int(i)
    if stetje % 4 == 2:
        print(0)
    else:
        print("Jedi macke")


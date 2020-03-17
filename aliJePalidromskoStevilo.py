"""

def aliJePalidromskoStevilo(x):
    y = x
    vsota = 0
    while y!=0:
        vsota = vsota*10 + y%10
        y = y//10
    if vsota == x:
        print("stevilo je palidromsko")
    else: 
        print("Stevilo ni palidromsko")
    
vnos = int(input("Vnesite stevilo: "))

aliJePalidromskoStevilo(vnos)

"""

def aliJeTroisko(x):W
    while x!=0:
        if 
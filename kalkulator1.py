vnos = "123"
seznam = []
while vnos!="":
    vnos = input("Vnesite stevilo")
    if vnos!="":
        seznam.append(int(vnos))
sestevanje = 0
for items in seznam:        
    sestevanje += items
print(sestevanje)
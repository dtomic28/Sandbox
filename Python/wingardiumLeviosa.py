stevilo = int(input("Vnesite stevilo: "))

vsota = 0
while stevilo!=0:
     stevka = stevilo%10
     vsota = vsota*10 + stevka
     print(int(vsota))
     stevilo = (stevilo-stevka)/10
  

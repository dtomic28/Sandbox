"""
info = int(input("Vnesite st: "))

for x in range(info):
  vrstica = ""
  for y in range(info):
    if x==info//2 or y==info//2 or x+y==info-1 or x==y:
        vrstica += "- "
    else:
        vrstica += "0 "
  print(vrstica)
"""
"""
vnos = int(input("Vnesite st: "))

for x in range(vnos, 0, -1):
  vrstica = ""
  for y in range(vnos, 0, -1):
    if x > vnos/2:
      vrstica += str(x) + " "
    else:
      vrstica += "0 "
  print(vrstica)
  """

def pretvoriV2(a):
  vsota = 0
  mnozenje = 1
  while a!=0:
    vsota += (a%2) * mnozenje
    mnozenje *= 10
  print(vsota)

pretvoriV2(121)

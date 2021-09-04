def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
def metoda(element):
    element = element[::-1]
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digit = "0123456789"
    niz = ""
    seznam = []
    stetje = 0
    prejsnja = ""
    multiplyer = 0
    for crke in element:
      if crke in digit and prejsnja in digit:
          multiplyer = str(multiplyer)
          multiplyer += crke
          multiplyer = int(multiplyer)
      elif crke in digit and prejsnja not in digit:
        multiplyer = int(crke)
      elif crke.isdigit==True and prejsnja==0:
        multiplyer = str(multiplyer)
        multiplyer = crke + "0"
        multiplyer = int(multiplyer)
      elif crke not in lowercase:
        niz += crke
        if multiplyer>1:
          while stetje!=multiplyer:
            seznam.append(niz[::-1])
            stetje += 1
          stetje = 0
        else:
          seznam.append(niz[::-1])
        niz = ""
        multiplyer = 0
      elif crke in lowercase:
        niz += crke
    
    printed = []
    for i in seznam:
        stevec=0
        for j in seznam:
            if i==j:
                stevec += 1
        seznam = remove_values_from_list(seznam, i)
        if i not in printed:
          print(i + "(" + str(stevec) + ")")
          printed.append(i)

metoda("C6H10OH")
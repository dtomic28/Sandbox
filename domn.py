import random
import os
import time
koncano = False
zmaga2 = 0
zmaga1 = 0
igralec = 1          
vsepoteze = 0     
konecpre = 0
miza1={
'A1': ' ', 'A2': ' ', 'A3': ' ', 'A4': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ', 'B4': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' ', 'C4': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' ', 'D4': ' ',
        
}
miza2={
'A1': ' ', 'A2': ' ', 'A3': ' ', 'A4': ' ', 'A5': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ', 'B4': ' ', 'B5':' ',
    'C1': ' ', 'C2': ' ', 'C3': ' ', 'C4': ' ', 'C5': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' ', 'D4': ' ', 'D5': ' ',
    'E1': ' ', 'E2': ' ', 'E3': ' ', 'E4': ' ', 'E5': ' ',
        
}

miza4x4=["","","","","","","","","",""]
miza5x5=["","","","","","","","","",""]
igralec1=""
igralec2=""
def meni():
  print("križci und krošci")
  print("pozdravljen/a igralec/ca/ka/ke")
  print('opcije: 4x4; test; 5x5')
  izbor=input("izberi velikost igre: ")
  test=""
  if izbor == 'test':
   os.system('clear') 
   prev2()
  elif izbor== 'igraj':
    os.system('clear') 
    imena()
   
  else:
   print("posksi znova")  
   time.sleep(2.4)
   os.system('clear') 
   meni()
 
def imena():
  igralec1=input("vnesi ime igralca1:")
  igralec1=igralec1
  os.system('clear') 
  igralec2=input("vnesi ime igralca2:")
  os.system('clear') 
  print("igralec1 je:",igralec1)
  print("igralec2 je:",igralec2)
  imena1=igralec1
  imena2=igralec2
  time.sleep(2.4)
  prev()
def imena2():
  igralec1=input("vnesi ime igralca1:")
  igralec1=igralec1
  os.system('clear') 
  igralec2=input("vnesi ime igralca2:")
  os.system('clear') 
  print("igralec1 je:",igralec1)
  print("igralec2 je:",igralec2)
  imena1=igralec1
  imena2=igralec2
  time.sleep(2.4)
  prev()
def prev():
    global zmaga1
    global zmaga2
    if miza1['A1'] == 'X' and miza1['A2'] == 'X' and miza1['A3'] =='X' and miza1['A4'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza1['B1'] == 'X' and miza1['B2'] == 'X' and miza1['B3'] == 'X' and miza1['B4'] == 'X':
        print('zmagal je...')
        time.sleep(5)
        os.system('clear')
        print('igralec1')
        time.sleep(2.4)
        return 1
    if miza1['C1'] == 'X' and miza1['C2'] == 'X' and miza1['C3'] == 'X' and miza1['C4'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza1['A1'] == 'X' and miza1['B2'] == 'X' and miza1['C3'] == 'X' and miza1['D1'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        zmaga1= zmaga1 + 1
        return 1
    if miza1['A1'] == 'X' and miza1['B1'] == 'X' and miza1['C1'] == 'X' and miza1['D1'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza1['A2'] == 'X' and miza1['B2'] == 'X' and miza1['C2'] == 'X' and miza1['D2'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza1['A3'] == 'X' and miza1['B3'] == 'X' and miza1['C3'] == 'X' and miza1['D3'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1

    if miza1['A1'] == 'O' and miza1['A2'] == 'O' and miza1['A3'] == 'O'and miza1['A4'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1 
    if miza1['B1'] == 'O' and miza1['B2'] == 'O' and miza1['B3'] == 'O' and miza1['B4'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza1['C1'] == 'O' and miza1['C2'] == 'O' and miza1['C3'] == 'O' and miza1['C4'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza1['A1'] == 'O' and miza1['B2'] == 'O' and miza1['C3'] == 'O' and miza1['D3'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza1['A1'] == 'O' and miza1['B1'] == 'O' and miza1['C1'] == 'O' and miza1['D1'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza1['A2'] == 'O' and miza1['B2'] == 'O' and miza1['C2'] == 'O' and miza1['D4'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza1['A3'] == 'O' and miza1['B3'] == 'O' and miza1['C3'] == 'O' and miza1['D3'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
    if miza1['D1'] == 'O' and miza1['D2'] == 'O' and miza1['D3'] == 'O' and miza1['D4'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        
        return 1
    return 0
def prev2():
    if miza2['A1'] == 'X' and miza2['A2'] == 'X' and miza2['A3'] =='X' and miza2['A4'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['B1'] == 'X' and miza2['B2'] == 'X' and miza2['B3'] == 'X' and miza2['B4'] == 'X':
        print('zmagal je...')
        time.sleep(5)
        os.system('clear')
        print('igralec1')
        time.sleep(2.4)
        return 1
    if miza2['C1'] == 'X' and miza2['C2'] == 'X' and miza2['C3'] == 'X' and miza2['C4'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['A1'] == 'X' and miza2['B2'] == 'X' and miza2['C3'] == 'X' and miza2['D1'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['A1'] == 'X' and miza2['B1'] == 'X' and miza2['C1'] == 'X' and miza2['D1'] == 'X' and miza2['E1'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['A2'] == 'X' and miza2['B2'] == 'X' and miza2['C2'] == 'X' and miza2['D2'] == 'X' and miza2['E2'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['A3'] == 'X' and miza2['B3'] == 'X' and miza2['C3'] == 'X' and miza2['D3'] == 'X' and miza2['E3'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
        return 1
    if miza2['A4'] == 'X' and miza2['B4'] == 'X' and miza2['C4'] == 'X' and miza2['D4'] == 'X' and miza2['E4'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1
    if miza2['A5'] == 'X' and miza2['B5'] == 'X' and miza2['C5'] == 'X' and miza2['D5'] == 'X' and miza2['E5'] == 'X':
        print('zmagal je igralec 1!')
        zmaga1= zmaga1 + 1

    if miza2['A1'] == 'O' and miza2['A2'] == 'O' and miza2['A3'] == 'O'and miza2['A4'] == 'O' and miza2['A5'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1 
    if miza2['B1'] == 'O' and miza2['B2'] == 'O' and miza2['B3'] == 'O' and miza2['B4'] == 'O' and miza2['B5'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza2['C1'] == 'O' and miza2['C2'] == 'O' and miza2['C3'] == 'O' and miza2['C4'] == 'O' and miza2['C5'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza2['A1'] == 'O' and miza2['B2'] == 'O' and miza2['C3'] == 'O' and miza2['D4'] == 'O' and miza2['E5'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza2['A1'] == 'O' and miza2['B1'] == 'O' and miza2['C1'] == 'O' and miza2['D1'] == 'O' and miza2['E1'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza2['A2'] == 'O' and miza2['B2'] == 'O' and miza2['C2'] == 'O' and miza2['D2'] == 'O' and miza2['E2'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        return 1
    if miza2['A3'] == 'O' and miza2['B3'] == 'O' and miza2['C3'] == 'O' and miza2['D3'] == 'O' and miza2['E3'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
    if miza2['D1'] == 'O' and miza2['D2'] == 'O' and miza2['D3'] == 'O' and miza2['D4'] == 'O' and miza2['E5'] == 'O':
        print('zmagal je igralec 2')
        zmaga2= zmaga2 + 1
        
        return 1
    return 0
print('opcija 1')
print(' ____')
print('|4x4|')
print(' ⎻⎻⎻⎻')
print('|A1|A2|A3|A4|')
print('|- +- +- +- |')
print('|B1|B2|B3|B4|')
print('|- +- +- +- |')
print('|C1|C2|C3|C4|')
print('|- +- +- +- |')
print('|C1|D2|D3|D4|')
print('***************************')
meni()
zmaga2 = 0
zmaga1 = 0
os.system('clear')
print('opcije 4x4 ali 5x5')
izbor=input('izberi velikost: ') 
while koncano == False:
 while True:
  if izbor == '4x4':
    print('__1_2_3_4_')
    print('A|'+miza1['A1']+'|'+miza1['A2']+'|'+miza1['A3']+'|'+miza1['A4']+'|')
    print('-+-+-+-+-|')
    print('B|'+miza1['B1'] + '|' + miza1['B2'] + '|' + miza1['B3']+'|'+miza1['B4']+'|')
    print('-+-+-+-+-|')
    print('C|'+miza1['C1'] + '|' + miza1['C2'] + '|' + miza1['C3']+'|'+miza1['C4']+'|')
    print('-+-+-+-+-|')
    print('D|'+miza1['D1'] + '|' + miza1['D2'] + '|' + miza1['D3']+'|'+miza1['D4']+'|')
    print('⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻')
    konecpre = prev()
    if vsepoteze == 16 or konecpre == 1:
        break
    while True:  
        if igralec == 1:  
            poteza_p1t = input('vnesi potezo igralec1: ')
            if poteza_p1t.upper() in miza1 and miza1[poteza_p1t.upper()] == ' ':
                miza1[poteza_p1t.upper()] = 'X'
                os.system('clear') 
                igralec = 2
                break
            else:
                print('neki nisi prav natipku poskusi znova')
                continue
        else:
            p2_input =input("{} vnesi potezo: ".format(igralec1))
            if p2_input.upper() in miza1 and miza1[p2_input.upper()] == ' ':
                miza1[p2_input.upper()] = 'O'
                os.system('clear')
                igralec = 1
                break
            else: 
                print('neki nisi prav natipku poskusi znova')
                continue
    vsepoteze += 1
    print('***************************')
    print()
  elif izbor == '5x5':
    print('__1_2_3_4_')
    print('A|'+miza2['A1']+'|'+miza2['A2']+'|'+miza2['A3']+'|'+miza2['A4']+'|'+miza2['A5']+'|')
    print('-+-+-+-+-|')
    print('B|'+miza2['B1'] + '|' + miza2['B2'] + '|' + miza2['B3']+'|'+miza2['B4']+'|'+miza2['B5']+'|')
    print('-+-+-+-+-|')
    print('C|'+miza2['C1'] + '|' + miza2['C2'] + '|' + miza2['C3']+'|'+miza2['C4']+'|'+miza2['C5']+'|')
    print('-+-+-+-+-|')
    print('D|'+miza2['D1'] + '|' + miza2['D2'] + '|' + miza2['D3']+'|'+miza2['D4']+'|'+miza2['D5']+'|')
    print('⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻')
    konecpre = prev2()
    if vsepoteze == 25 or konecpre == 1:
        break
    while True:  
      if igralec == 1:  
            poteza_p1t = input('vnesi potezo igralec 1: ')
            if poteza_p1t.upper() in miza1 and miza1[poteza_p1t.upper()] == ' ':
                miza2[poteza_p1t.upper()] = 'X'
                os.system('clear') 
                igralec = 2
                break
            else:
                print('neki nisi prav natipku poskusi znova')
                continue
      else:
            p2_input =input("{} vnesi potezo igralec 2: ".format(igralec1))
            if p2_input.upper() in miza1 and miza1[p2_input.upper()] == ' ':
                miza2[p2_input.upper()] = 'O'
                os.system('clear')
                igralec = 1
                break
            else: 
                print('neki nisi prav natipku poskusi znova')
                continue
    vsepoteze += 1
    print('***************************')
    print()   
    if zmaga1 == 3 or zmaga2 ==3:
        print('konec igre!!!')
        koncano = True
    miza1={
        'A1': ' ', 'A2': ' ', 'A3': ' ', 'A4': ' ',
            'B1': ' ', 'B2': ' ', 'B3': ' ', 'B4': ' ',
            'C1': ' ', 'C2': ' ', 'C3': ' ', 'C4': ' ',
            'D1': ' ', 'D2': ' ', 'D3': ' ', 'D4': ' ',

        }
    miza2={
    'A1': ' ', 'A2': ' ', 'A3': ' ', 'A4': ' ', 'A5': ' ',
        'B1': ' ', 'B2': ' ', 'B3': ' ', 'B4': ' ', 'B5':' ',
        'C1': ' ', 'C2': ' ', 'C3': ' ', 'C4': ' ', 'C5': ' ',
        'D1': ' ', 'D2': ' ', 'D3': ' ', 'D4': ' ', 'D5': ' ',
        'E1': ' ', 'E2': ' ', 'E3': ' ', 'E4': ' ', 'E5': ' ',
            
    }

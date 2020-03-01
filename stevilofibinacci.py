"""
def sodoStevilka(x):
    for i in range(1, x+1):
        vrstica = ""
        for j in range(1, x+1):
            if i==x//2+1 or j==x//2+1 and i==x or i==1 or j==x or j==1:   
                vrstica += str(i)+""
            else:
                vrstica += "0 "
        print(vrstica)


vnos = int(input("Vnesite stevilo x: "))
sodoStevilka(vnos)
    
"""

from tkinter import *
root = Tk()

root.geometry = "300x400"






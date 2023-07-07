from os import system
import numpy as np

system("cls")

x1 = float(input("Inserisci il valore di x1: "))
x2 = float(input("Inserisci il valore di x2: "))
y1 = float(input("Inserisci il valore di y1: "))
y2 = float(input("Inserisci il valore di y2: "))

distanza = np.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2)

print(f"La distanza tra i due punti è:{distanza}")
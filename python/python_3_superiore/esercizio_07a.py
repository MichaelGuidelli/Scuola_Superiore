from os import system
import numpy as np

system("cls")

i = 0
ascisse = []
ordinate = []

while i < 10:
    
    ascisse.append(i)
    ordinate.append(np.power(i, 2))
    i += 1

print(f"Numeri nella lista Ascisse: {ascisse}", f"Numeri nella lista Ordinate: {ordinate}", sep = "\n")
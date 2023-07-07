from random import randrange
from os import system
import numpy as np

system("cls")

def cerchio(raggio: int):
   
    area = np.pi * np.power(raggio, 2)
    perimetro = 2 * np.pi * raggio
    return area, perimetro
    
risultato = list(cerchio(raggio = randrange(1, 10)))
print(f"Il valore della tua area è: {risultato[0]}", f"Il valore della tuo perimetro è {risultato[1]}", sep = "\n")
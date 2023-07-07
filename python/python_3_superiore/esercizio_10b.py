from os import system
from random import randrange

system("cls")

def scambio(numeri: int, posto_1: int, posto_2: int):
    
    x = numeri[posto_1]
    numeri[posto_1] = numeri[posto_2]
    numeri[posto_2] = x
    
    return numeri

numeri = [randrange(10) for i in range(10)]
posto_1= int(input("Inserisci il primo posto da scambiare: "))
posto_2 = int(input("Inserisci il secondo posto da scambiare: "))
print(f"Lista prima dello scambio: {numeri}")
risultato = scambio(numeri, posto_1, posto_2)
print(f"Lista dopo lo scambio: {risultato}")
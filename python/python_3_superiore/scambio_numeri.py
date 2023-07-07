from os import system
from random import randrange

system("cls")

numeri = []

for i in range(10):
    numeri.append(randrange(0,10))

print(f"Lista principale:{numeri}")

x = numeri[0]
numeri[0] = numeri[9]
numeri[9] = x

print(f"Lista con il primo e l'ultimo numero scambiati:{numeri}")
from random import randrange
from os import system

system("cls")

a_list = [randrange(50) for i in range(10)]

for i, v in enumerate(a_list):
    if i % 2 == 0:
        print(f"Indice: {i}, elemento: {v}")
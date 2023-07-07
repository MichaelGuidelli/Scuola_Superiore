from os import system
from obj import *

system("cls")

auto_1 = Auto("Mustang", "Blu")
auto_2 = Auto("Ferrari", "Rosso")
auto_3 = Auto("Audi", "Bianco")

print(auto_1.carta_di_circolazione())
print(auto_2.carta_di_circolazione())
print(auto_3.carta_di_circolazione())
print(f"Numero di auto: {Auto.numero_di_auto}")
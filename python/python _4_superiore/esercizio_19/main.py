from os import system
from obj import *

system('cls')

concorrenti = [Auto("Audi", "Bianco", 30_000), Auto("Ferrari", "Rosso", 120_000), Auto("Range Rover", "Nero", 60_000), Auto("Lamborghini", "Verde", 500_000)]

for auto in range(len(concorrenti)):
    
    if auto == len(concorrenti) - 1: print(f"{concorrenti[auto].carta_di_circolazione() + ' ed elettrico'}")
    
    else: print(concorrenti[auto].carta_di_circolazione())
    
print(f"Macchine in gara: {Auto.macchine_in_gara}")
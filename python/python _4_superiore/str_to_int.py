from random import randrange
from os import system

system("cls")

stringa_vuota = "" # Stringa vuota.
with open("file.txt", "w") as file: # Creazione file .txt.
    for i in range(20):
        stringa_vuota += str(randrange(50)) + " " # 20 numeri tra 1 e 50 spaziati tra di loro.
    file.write(stringa_vuota)

with open("file.txt", "r") as file: # Lettura file .txt.
    file = file.read()
    print(file, type(file)) # Print lista prima della conversione.
    
text_out = [int(i) for i in file.strip().split()] # Conversione del dato sfruttando l'indice, 
#il metodo strip eliminerà gli spazi, la funzione split ritornerà una lista con all'interno i numeri del file.
print(text_out, type(text_out[0])) # Print lista dopo la conversione.

"""
Senza list comprehension.

for i in range(len(alist)):
    alist[i] = int(alist[i])

"""
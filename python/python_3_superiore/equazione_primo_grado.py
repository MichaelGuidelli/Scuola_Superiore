from os import system # Dalla libreria os importo system.

system ("cls") # Comando per pulire la consore.

a = float(input("Inserisci il valore di A: ")) # Input di a. 
b = float(input("Inserisci il valore di B: ")) # Input di b. 

if a == 0 and b != 0: print("Equazione impossibile") # Controllo se a è uguale a 0 e se b non è uguale a 0.
    
elif a == 0 and b == 0: print("Equazione indefinita") # Controllo se a e b sono uguali a 0.

else:
    x = - b / a # Operazione matematica.
    print(f"Il valore della tua equazione è {x}") # Output di x. 
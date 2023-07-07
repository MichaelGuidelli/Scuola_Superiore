from os import system # Importo system da os.

system("cls") # Comando per pulire la console.

def area(base: int, altezza: int): # Creo la definizione per calcolare l'Area.
    area = base * altezza # Calcolo matematico per l'Area.
    return area # Ritorno il valore di Area.

def perimetro (base: int, altezza: int): # Creo la definizione per calcolare il Perimetro.
    perimetro = 2 * base + 2 * altezza  # Calcolo matematico per il Perimetro.
    return perimetro # Ritorno il valore del Perimetro.

base = float(input("Inserisci il valore della tua base: ")) # Input della base.
altezza = float(input("Inserisci i lvalore della tua altezza: ")) # Input dell'Altezza.
area = area(base, altezza) # Richiamo la funzione Area.
perimetro = perimetro(base, altezza)  # Richiamo la funzione Perimetro.

# Output di perimetro e area.
print(f"Il valore del tuo Perimetro è: {perimetro}", f"Il valore della tua area è: {area}", sep = "\n")
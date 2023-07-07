base = input("Inserisci la Base: ") # Input della base.
altezza = input("Inserisci il Perimetro: ") # Input dell'area.

base = float(base) # Trasformo base da int a float. 
altezza = float(altezza) # Trasformo altezza da int a float.

perimetro = 2 * base + 2 * altezza # Operazione geometrica per ricavare il perimetro.
area = base * altezza # Operazione geometrica per ricavare l'area.

print(f"Il valore della tuo Perimetro è: {perimetro}" ) # Output del perimetro.
print(f"Il valore della tua Area: {area}") # Output dell'area.
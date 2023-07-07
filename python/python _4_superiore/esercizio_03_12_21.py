from os import system

system('cls')

studenti = {
    
    "Guidelli": 1641,
    "Corsetti": 1432,
    "Di Tota": 1223,
    "Facciuti": 5532,
    "Peruggi": 2234,
    "Lista": 1076,
    "Manna": 2464,
    "Rossi": 8888,
    "Bianchi": 2568,
    "Esposito": 9865
    
}

print(f"Lista Studenti: {studenti}")
print(f"Cognomi ordinati: {sorted(studenti.keys())}")
print(f"Matricole ordinate: {sorted(studenti.values())}")
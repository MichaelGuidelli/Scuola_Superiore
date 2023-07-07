from os import system # Importo system da os.

system("cls") # Comando per pulire la console.

nome = input("Inserisci il tuo nome: ") # Input del nome.
cognome = input("Inserisci il tuo cognome: ") # Input del cognome.
età = int(input("Inserisci la tua età: ")) # Input dell'età.

print(f"Mi chiamo {nome} {cognome}, e la mia età tra 10 anni sarà {età + 10}")  #Output 
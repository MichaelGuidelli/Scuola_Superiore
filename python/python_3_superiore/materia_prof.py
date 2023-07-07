from os import system

system("cls")

nome = input("Inserisci il nome cognome del professore: ").title() # La funzione .title trasforma la prima lettera di ogni parola in maiuscolo.

if nome == "Arcella": print("Il prof Arcella insegna informatica")
elif nome == "Di Domenico": print("La prof Di Domenico insegna Italiano e Storia")
elif nome== "Vitiello": print("La prof Vitiello Insegna Inglese")
elif nome == "Vilone": print("Il prof Vilone insegna Telecomunicazioni")
elif nome== "Ragosa": print("Il prof Ragosa insegna Sistemi e reti e Tecnologia Progettazione Informatica ")
elif nome == "Cauteruccio": print("Il prof Cauteruccio insegna  Matematica")
else: print(f"Il Cognome inserito {nome} non è di un professore della 3BSE")
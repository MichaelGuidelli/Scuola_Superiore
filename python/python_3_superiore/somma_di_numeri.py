from os import system 

system("cls")

def somma(n: int) -> None:
    somma = 0
    if n == 0: print("Il numero inserito è neutrale")
    elif n < 0: print("Il numero inserito è negativo")
    else:
        while n > 0:
            num = int(input("Inserisci numero: "))
            somma += num
            n -= 1
        print(f"Il risultato è {somma}")

somma(n = int(input("Quanti numeri vuoi sommare? ")))
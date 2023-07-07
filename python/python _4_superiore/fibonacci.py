from functools import cache
from os import system
import time

system("cls")

def fibonacci_no_cache(termini: int):
    return termini if termini <= 1 else fibonacci_no_cache(termini - 1) + fibonacci_no_cache(termini - 2)

@cache
def fibonacci_cache(termini: int):
    return termini if termini <= 1 else fibonacci_cache(termini - 1) + fibonacci_cache(termini - 2)

def controllo_input():
    while True:
        try:
            termini = int(input("Inserisci i termini: "))
            if termini <= 0:
                print("Errore, Hai inserito un numero negativo ed è stato trasformato in positivo!")
                termini = abs(termini)
        except ValueError:
                print("Errore, non puoi inserire delle stringhe!")
        else: 
            break
    
    return termini  

def main() -> None:

    termini = controllo_input()

    print("Sequenza di Fibonacci senza cache decorator: ")
    inizio = time.time()
    for termine in range(termini): print(fibonacci_no_cache(termine))
    fine = time.time()
    print(f"Tempo di esecuzione della funzione Fibonacci senza cache decorator: {fine - inizio}")
    
    print("Sequeza di Fibonacci con cache decorator: ")
    inizio_ = time.time()
    for termine in range(termini):  print(fibonacci_cache(termine))
    fine_ = time.time()
    print(f"Tempo di esecuzione della funzione Fibonacci con cache decorator: {fine_ - inizio_}") 
    
main()
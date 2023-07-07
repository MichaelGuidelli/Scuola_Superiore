from os import system
import numpy as np

system('cls')

def neurone(dati: float):
    return dati[0] * dati[1] + dati[2] * dati[3] + dati[4]

def sigmoide(result_neurone: float) -> None:
   print(f"Risultato: {1 / (1 + np.exp(- (result_neurone)))}")

def controllo_input():
    peso_1, peso_2, bias = np.random.random(), np.random.random(), np.random.random()
    while True:
        try:   
            massa, lunghezza = [float(i) for i in input("Inserisci massa e lunghezza: ").split()] 
            if massa <= 0 or lunghezza <= 0: 
                print("Errore, inserisci numeri positivi!")
                controllo_input()            
        except ValueError:  
                print("Errore, non puoi inserire delle stringhe oppure non hai inserito abbastanza dati!")
        else:
            break
    
    return [massa, peso_1, lunghezza, peso_2, bias]
 
sigmoide(neurone(controllo_input()))
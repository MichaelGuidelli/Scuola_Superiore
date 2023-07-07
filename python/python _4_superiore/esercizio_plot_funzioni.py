import matplotlib.pyplot as plt 
from os import mkdir, system
import numpy as np 

system("cls")

def esponenziale_positiva(intervallo: float):
    return np.exp(intervallo)

def esponenziale_negativa(intervallo: float):
    return np.exp(- intervallo)

def potenza_di_due(intervallo: float):
    return np.power(intervallo, 2)

def potenza_di_tre(intervallo: float):
    return np.power(intervallo, 3)

def seno(intervallo: float):
    return np.sin(intervallo)

def coseno(intervallo: float):
    return np.cos(intervallo)

def grafico(intervallo: float, results: float, titolo_plot: str, nome_cartella: str) -> None:
    
    plt.plot(intervallo, results)
    plt.title(titolo_plot)
    plt.tight_layout()
    plt.savefig(f"{nome_cartella}/{titolo_plot}")
    plt.show()
    
def main() -> None:
        
    try:
        nome_cartella = "cartella_funzioni"
        mkdir(nome_cartella)
    except FileExistsError:
        nome_cartella = str(input("Inserisci il nome della cartella: "))
        mkdir(nome_cartella)   
        
    intervallo = np.linspace(- 10, 10, 100)
    grafico(intervallo, esponenziale_positiva(intervallo), "Esponenziale Positiva", nome_cartella)
    grafico(intervallo, esponenziale_negativa(intervallo), "Esponenziale Negativa", nome_cartella)
    grafico(intervallo, potenza_di_due(intervallo), "Potenza Di 2", nome_cartella)
    grafico(intervallo, potenza_di_tre(intervallo), "Potenza Di 3", nome_cartella)
    grafico(intervallo, seno(intervallo), "Seno", nome_cartella)
    grafico(intervallo, coseno(intervallo), "Coseno", nome_cartella)
    
main()
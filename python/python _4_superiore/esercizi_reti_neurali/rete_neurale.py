import matplotlib.pyplot as plt
from os import system
import numpy as np 

system("cls")

def sigmoide(previsione: float):
    return 1 / (1 + np.exp(- previsione))

def derivata_parziale(previsione: float, obiettivo: int, peso: float):
    return (2 * (previsione - obiettivo)) * (previsione * (1 - previsione)) * peso

def calcolo_affidabilità(previsione_riuscita: float, totale: int):
    return previsione_riuscita / totale * 100

def allenamento(data_set_allenamento):
    
    np.random.seed(1)
    
    peso_1, peso_2, bias = np.random.random(), np.random.random(), np.random.random()
    learning_rate = 0.1
    
    for epoca in range(10_000):
        
        indice_casuale = np.random.randint(0, len(data_set_allenamento) - 1)
        gatto_random = data_set_allenamento[indice_casuale]
        
        neurone = gatto_random[0] * peso_1 + gatto_random[1] * peso_2 + bias
        previsione = sigmoide(neurone)
        obiettivo = gatto_random[2]
        
        peso_1 -= learning_rate * derivata_parziale(previsione, obiettivo, gatto_random[0])
        peso_2 -= learning_rate * derivata_parziale(previsione, obiettivo, gatto_random[1])
        bias -= learning_rate * derivata_parziale(previsione, obiettivo, 1)
        
    return peso_1, peso_2, bias

def tests(data_set_allenamento, data_set_prova):
    
    affidabilità = 0
    peso_1, peso_2, bias = allenamento(data_set_allenamento)
    
    risultati = []
    for gatto in data_set_prova:
        previsione = sigmoide(gatto[0] * peso_1 + gatto[1] * peso_2 + bias)  
        risultati.append(f"{'Giungla (0)' if round(previsione) == 0 else 'Sabbie (1)' }, Previsione: {previsione}")
        if abs(round(previsione)) == gatto[2]: affidabilità += 1
        
    for risultato in risultati: print(risultato)
    
    print(f"Affidabilità della Rete: {calcolo_affidabilità(affidabilità, len(data_set_prova))}%")
    
    return calcolo_affidabilità(affidabilità, len(data_set_prova))

def grafico(nome: str, results: int, colore: float, spessore: float) -> None:
    
    plt.figure(figsize = (10, 5))
    plt.title("Affidabilità Della Rete Neurale")
    plt.bar(nome, results, color = colore, width = spessore, edgecolor = "Black")
    plt.ylabel("Percentuale")

    for bar in range(len(results)): plt.text(bar, results[bar], f"{results [bar]}%", ha = "center", va = "bottom")
    
    plt.tight_layout()
    plt.show()

def main() -> None:
    
    data_set_talarico = [
        [9, 7.0, 0],
        [2, 5.0, 1],
        [3.2, 4.94, 1],
        [9.1, 7.46, 0],
        [1.6, 4.83, 1],
        [8.4, 7.46, 0],
        [8, 7.28, 0],
        [3.1, 4.58, 1],
        [6.3, 9.14, 0],
        [3.4, 5.36, 1]
    ] 
    
    data_set_prova = [
        [8, 6.99, 0],
        [3, 5.5, 1],
        [3.3, 4.99, 1],
        [9, 7.45, 0],
        [1.8, 4.88, 1],
        [8.6, 7, 0],
        [7.50, 7.30, 0],
        [2.99, 4.60, 1],
        [6.5, 9, 0],
        [3.5, 5.40, 1]
    ]

    data_dict = {"Dataset Talarico": tests(data_set_talarico, data_set_talarico),
                 "Dataset Talarico[:5]": tests(data_set_talarico[:5], data_set_talarico[5:]),
                 "Dataset Prova": tests(data_set_prova, data_set_prova),
                 "Dataset Prova[:5]": tests(data_set_prova[:5], data_set_prova[5:]),
                 "Dataset Talarico/Prova": tests(data_set_talarico, data_set_prova)}

    grafico(list(data_dict.keys()), list(data_dict.values()), (0.2, 0.4, 0.6, 0.6), 0.5)

main()
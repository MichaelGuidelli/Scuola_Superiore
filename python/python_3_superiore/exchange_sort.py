from random import randrange
from os import system
import matplotlib.pyplot as plt
from math import ceil

system("cls") 

def exchange_sort(lista: int):
    
    if len(lista) <= 1: return lista, 0
    
    scambi_effettuati = 0
    
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                scambi_effettuati += 1
                             
    return lista, scambi_effettuati

lunghezza = int(input("Scegli la lunghezza: "))
range = int(input("Scegli il range: "))
lista_random = [randrange(range) for i in range(lunghezza)]
lista_disordinata = [randrange(range) for i in range(lunghezza)]
lista_disordinata.sort()
lista_disordinata.reverse()

print(f"Lista random prima dello scambio: {lista_random[:50]} \n")
print(f"Lista disordinata prima dello scambio: {lista_disordinata[:50]} \n")

es_data_random = exchange_sort(lista_random)
es_data_lista_disordinata = exchange_sort(lista_disordinata)

print("Risultati e scambi effettuati dall'Exchange sort:")
print(f"Lista random dopo lo scambio: {es_data_random[0][:50]}", f"Numero di scambi effettuati dalla la lista random: {es_data_random[1]}",sep = "\n")
print(f"Lista disordinata dopo lo scambio: {es_data_lista_disordinata[0][:50]}", f"Numero di scambi effettuati dalla lista disordinata: {es_data_lista_disordinata[1]}", sep = "\n")

nomi_liste = ["Lista Random", "Lista Disordinata"]
scambi_es = [es_data_random[1], es_data_lista_disordinata[1]]

for i in range(len(scambi_es)):
    plt.text(i, scambi_es [i], scambi_es [i], ha = "center", va = "bottom") # ha = alliniamento orizzontale, va = alliniamento verticale
 
plt.title("Scambi effettuati dall'Exchange sort")
plt.bar(nomi_liste, scambi_es)
min = min(scambi_es)
max = max(scambi_es)
plt.ylim([ceil(min-0.5*(max-min)), ceil(max+0.5*(max-min))])
plt.tight_layout()
plt.show()
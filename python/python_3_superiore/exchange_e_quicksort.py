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

def quick_sort(lista: int):
    
    if len(lista) <= 1: return lista
    
    left, center, right = [], [], []
    pivot = lista[-1]
    
    for i in lista:
        if i < pivot: left.append(i)
        elif i == pivot: center.append(i)
        else: right.append(i)
    
    lista = min + center + right
    return lista
    
lunghezza = int(input("Scegli la lunghezza: "))
range = int(input("Scegli il range: "))
lista_random = [randrange(range) for i in range(lunghezza)]
lista_disordinata = [randrange(range) for i in range(lunghezza)]
lista_disordinata.sort()
lista_disordinata.reverse()

print(f"Lista random prima dello scambio: {lista_random[:50]}")
print(f"Lista disordinata prima dello scambio: {lista_disordinata[:50]}"), print("")

es_data_random = exchange_sort(lista_random)
es_data_lista_disordinata = exchange_sort(lista_disordinata)

print("Risultati e scambi effettuati dall'Exchange sort:")
print(f"Lista random dopo lo scambio: {es_data_random[0][:50]}", f"Numero di scambi effettuati dalla la lista random: {es_data_random[1]}", sep = "\n"), print("")
print(f"Lista disordinata dopo lo scambio: {es_data_lista_disordinata[0][:50]}", f"Numero di scambi effettuati dalla lista disordinata: {es_data_lista_disordinata[1]}", sep = "\n"), print("")

qs_data_random = quick_sort(lista_random)
qs_data_lista_disordinata = quick_sort(lista_disordinata)

print("Risultati e scambi del Quick sort:")
print(f"Lista random dopo lo scambio: {qs_data_random[:50]}"), #   f"Numero di scambi effettuati dalla la lista random: {QSdataRandom[1]}", sep = "\n"), print("")
print(f"Lista disordinata dopo lo scambio: {qs_data_lista_disordinata[:50]}") #     f"Numero di scambi effettuati dalla lista disordinata: {QSdataListaDisordinata[1]}", sep = "\n")

nomi_liste = ["LRES", "LDES"] #  ["LRQS", "LDQS"]
scambi = [es_data_random[1], es_data_lista_disordinata[1]] #  [QSdataRandom[1], QSdataListaDisordinata[1]]

for i in range(len(scambi)):
    plt.text(i, scambi[i], scambi[i], ha = "center", va = "bottom") # ha = alliniamento orizzontale, va = alliniamento verticale

plt.bar(nomi_liste[0], es_data_random[1], color = "Red", label = "Exchange Sort")
plt.bar(nomi_liste[1], es_data_lista_disordinata[1], color = "Red")
# plt.bar(NomiListe[2], QSdataRandom[1], color = "Blue", label = "Quick Sort")
# plt.bar(NomiListe[3], QSdataListaDisordinata[1], color = "Blue")
min = min(scambi)
max = max(scambi)
plt.ylim([ceil(min - 0.5 * (max - min)), ceil(max + 0.5 * (max-min))])
plt.title("Scambi effettuati dai Sort:")
plt.tight_layout()
plt.legend()
plt.show()
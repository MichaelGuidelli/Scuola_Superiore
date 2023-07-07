from os import system

system('cls')

"""
! Non potendo utilizzare librerie matematiche al momento il codice non semplifica le frazioni. 
Risolvere il seguente sistema lineare con il metodo di Cramer.
3x + 2y = -1
x - y = 1

Risultato = [(1/5; -4/5)]
"""

def cramer(coefficiente: int, termine_noto: int) -> None:
    determinante = coefficiente[0] * coefficiente[3] - coefficiente[1] * coefficiente[2]
    x = termine_noto[0] * coefficiente[3] - coefficiente[1] * termine_noto[1]
    y = coefficiente[0] * termine_noto[1] - termine_noto[0] * coefficiente[2]
     
    print(f"Risultato:\nX: {x}|{determinante} \nY: {y}|{determinante}")

coefficienti = []
termini_noti = []

for i in range(4): coefficienti.append(int(input(f"Inserisci il coefficiente numero {i + 1}: ")))
for i in range(2): termini_noti.append(int(input(f"Inserisci il termine noto {i + 1}: ")))

cramer(coefficienti, termini_noti)
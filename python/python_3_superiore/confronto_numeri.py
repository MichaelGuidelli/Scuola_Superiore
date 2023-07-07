from os import system

system("cls")

k = int(input("Inserisci il valore di K: "))
n = int(input("Quanti numeri vuoi confrontare: "))
maggiori = 0
minori = 0
uguali =  0

while n > 0:
    num = int(input("Inserisci numero: "))
    n -= 1
    
    if num > k:
        maggiori += 1
    
    elif k > num:
        minori += 1
    
    elif num == k:
        uguali += 1
        
        
print(f"I numeri maggiori di K sono: {maggiori}", f"I numeri minori di K sono {minori}", f"I numeri uguali a K sono: {uguali}" , sep = "\n")
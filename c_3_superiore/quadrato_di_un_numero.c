#include <stdio.h>

int square(int x) /* Creo la funzione per calcolare il quadrato di un numero */
{
    return x * x; /* Operazione matematica */
}

int main()  /* Inizio il programma principale */
{
    int x; /* Dichiaro x come un intero */
    x = square(5); /* Assegno ad x la funzione del quadrato con il numero 5 da calcolare */
    printf("Quadrato di 5: %d", x); /* Output del programma */
}
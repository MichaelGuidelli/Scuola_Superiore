#include <stdio.h>

int main()
{
    int a, b;
    
    printf("Inserisci il valore di A: ");
    scanf("%d", &a);
    printf("Inserisci il valore di B: ");
    scanf("%d", &b);

    if(b == 0)
    {
        printf("B è neutro");
    }
    else if (b < 0)
    {
       printf("B è un numero negativo \n");
    }
    else
    {
        printf("B è un numero positivo \n");
    }

    if(a == 0)
    {
        printf("A è neutro");
    }
    else if(a % 2 == 0)
    {
         printf("A è un numero pari \n");
    }
    else
    {
        printf("A è un numero dispari \n");
    }

    if(a == b)
    {
        printf("I due numeri sono uguali \n");
    }
    else if (a > b)
    {
       printf("A è maggiore di B \n");
    }
    else
    {
        printf("B è maggiore di A \n");
    }
    
}
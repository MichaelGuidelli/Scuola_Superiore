#include <stdio.h>

int Add(int a, int b)
{
    return a + b;
}

int Sot(int a, int b)
{
    return a - b;
}

int Mol(int a, int b)
{
    return a * b;
}

int Div(int a, int b)
{
    return a / b;
}

int main()
{
    int a, b;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    if(a == 0 || b == 0)
    {
        printf("Uno dei due numeri è uguale a zero \n");
    }

    else 
    {
        int x = Add(a, b);
        printf("Risultato Addizione: %d \n", x);

        int y = Sot(a, b);
        printf("Risultato Sottrazione: %d \n", y);

        int j = Mol(a, b);
        printf("Risultato Moltiplicazione: %d \n", j);

        int z = Div(a, b);
        printf("Risultato Divisione: %d \n", z);
    }
  
} 
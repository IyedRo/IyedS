#include <stdio.h>
#include <conio.h>
#include <stdbool.h>

bool isPrime(int num)
{
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (int i = 3; i * i <= num; i += 2)
    {
        if (num % i == 0) return false;
    }
    return true;
}

int main()
{
    char r;
    do
    {
        int ch;
        printf("Enter Any Number: ");
        scanf("%d", &ch);
        if (isPrime(ch))
        {
            printf("%d is a Prime Number.\n", ch);
        }
        else
        {
            printf("%d is not a Prime Number.\n", ch);
        }
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

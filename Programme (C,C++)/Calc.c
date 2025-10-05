#include <stdio.h>
#include <conio.h>

int main()
{
    char r;
    do
    {
        int a, b;
        char o;
        printf("Input Number: ");
        scanf("%d", &a);
        printf("Input Number: ");
        scanf("%d", &b);
        printf("Choose('+','-','/','*'): ");
        scanf(" %c", &o);
        if (o == '+')
        {
            printf("%d\n", a + b);
        }
        else if (o == '-')
        {
            printf("%d\n", a - b);
        }
        else if (o == '*')
        {
            printf("%d\n", a * b);
        }
        else if (o == '/')
        {
            if (b != 0)
            {
                printf("%d\n", a / b);
            }
            else
            {
                printf("Error: Division by zero!\n");
            }
        }
        else
        {
            printf("Invalid Input!\n");
        }
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <ctype.h>

void print_binary(unsigned char n)
{
    for(int i = 7; i >= 0; i--)
    {
        printf("%d", (n >> i) & 1);
    }
}

int main()
{
    char r;
    do
    {
        char input[100];
        char ch;
        printf("Input Character One: ");
        ch=_getch();
        printf("Converted: %c\n", ch);
        printf("ASCII Value (Decimal): %d\n", ch);
        printf("ASCII Value (Hexadecimal): %x\n", ch);
        printf("ASCII Value (Binary): ");
        print_binary(ch);
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

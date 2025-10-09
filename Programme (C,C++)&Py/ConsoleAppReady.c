#include <stdio.h>
#include <conio.h>

int main()
{
    char r='y';
    do
    {
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

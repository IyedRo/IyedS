#include <stdio.h>
#include <conio.h>

int main()
{
    char r;
    do
    {
        long long int kilobytes;
        printf("Input Number For KiloByte: ");
        scanf("%lld", &kilobytes);
        long long int Bytes = kilobytes * 1024;
        long long int Bits = Bytes * 8;
        printf("KiloByte To Bytes: %lld\n", Bytes);
        printf("Bytes To Bits: %lld\n", Bits);
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

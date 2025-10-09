#include <stdio.h>
#include <conio.h>
#include <math.h>

int main()
{
    char r;
    do
    {
        int n,sum;
        printf("N=");
        scanf("%d",&n);
        /*
        Methode '(n(n+1))/2'=='(n*n+n)/2' ;
        start with (0) if max impair 'n*((n+1)/2)' if max pair '(n*(n/2))+(n/2)';
        start with (1) if max impair '(n*((n-1)/2))+((n+1)/2)' if max pair '(n+1)*(n/2)';
        */
        sum=(n*n+n)/2;
        printf("Sum=%d\n",sum);
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

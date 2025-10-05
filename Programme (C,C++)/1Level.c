#include <stdio.h>
#include <conio.h>
#include <string.h>

int main()
{
    char r;
    do
    {
        // Type Case
        printf("====================\n");
        printf("%zu\n", sizeof(int));       // Typically 4
        printf("%zu\n", sizeof(float));     // Typically 4
        printf("%zu\n", sizeof(double));    // Typically 8
        printf("%zu\n", sizeof("string"));  // Size of string literal (7 bytes)
        // Test
        printf("====================\n");
        int num = 10;
        num = 20.5;  // Update but get int without float
        printf("%d;%zu\n", num, sizeof(num));
        float nums = 20.5;
        nums = 10;  // Update but stays float
        printf("%.1f;%zu\n", nums, sizeof(nums));
        double dob = 19.9;
        printf("%.1f;%zu\n", dob, sizeof(dob));
        float fl = 10.5 + 9.5;
        printf("%.1f;%zu\n", fl, sizeof(fl));
        printf("====================\n");
        char a = 'A';
        printf("%c;%d\n", a, (int)a);
        char b = 'B';  // C doesn't have 'auto' like C++
        printf("%c;%d\n", b, (int)b);
        printf("\nPress 'Y' To Repeat,Any To Exit: ");
        r=_getch();
        putchar('\n');
    }
    while(r=='Y'||r=='y');
    return 0;
}

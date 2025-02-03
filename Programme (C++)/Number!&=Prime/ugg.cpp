#include <iostream>

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
    int ch;

    std::cout << "Enter Any Number: ";
    std::cin >> ch;

    if (isPrime(ch))
    {
        std::cout << ch << " is a Prime Number." << std::endl;
    }
    else
    {
        std::cout << ch << " is not a Prime Number." << std::endl;
    }

    std::cout << "Press Enter to close...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

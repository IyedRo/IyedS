#include <iostream>

int main()
{
    int a, b;
    char o;

    std::cout << "Input Number: ";
    std::cin >> a;
    std::cout << "Input Number: ";
    std::cin >> b;
    std::cout << "Choose('+','-','/','*'): ";
    std::cin >> o;

    if (o == '+')
    {
        std::cout << a + b << std::endl;
    }
    else if (o == '-')
    {
        std::cout << a - b << std::endl;
    }
    else if (o == '*')
    {
        std::cout << a * b << std::endl;
    }
    else if (o == '/')
    {
        if (b != 0)
        {
            std::cout << a / b << std::endl;
        }
        else
        {
            std::cout << "Error: Division by zero!" << std::endl;
        }
    }
    else
    {
        std::cout << "Invalid Input!" << std::endl;
    }

    std::cout << "Press Enter to close...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

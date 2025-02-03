#include <iostream>

int main()
{
    long long int kilobytes;
    std::cout << "Input Number For KiloByte: ";
    std::cin >> kilobytes;
    long long int Bytes=kilobytes*1024;
    long long int Bits=Bytes*8;
    std::cout <<"KiloByte To Bytes: "<<Bytes<<std::endl;
    std::cout <<"Bytes To Bits: "<<Bits<<std::endl;

    std::cout << "Press Enter to close...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

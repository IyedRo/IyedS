#include <iostream>
#include <bitset>
#include <iomanip>

int main()
{
    std::string ch;
    std::cout<<"Input Character One: ";
    std::cin>>ch;
    while (ch.length()!=1)
    {
        std::cout<<"Please input only one character: ";
        std::cin>>ch;
    }
    int chr=int(ch[0]);
    std::bitset<8> binary(chr);
    std::cout<<"Converted: "<<ch<<std::endl;
    std::cout<<"ASCII Value (Decimal): "<<chr<<std::endl;
    std::cout<<"ASCII Value (Hexadecimal): "<<std::hex<<chr<<std::endl;
    std::cout<<"ASCII Value (Binary): "<<binary<<std::endl;

    std::cout << "Press Enter to close...";
    std::cin.ignore();
    std::cin.get();
    return 0;
}

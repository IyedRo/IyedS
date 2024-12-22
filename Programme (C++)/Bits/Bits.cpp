#include <iostream>
using namespace std;

int main()
{
    long long int kilobytes;
    cout << "Input Number For KiloByte: ";
    cin >> kilobytes;
    long long int Bytes=kilobytes*1024;
    long long int Bits=Bytes*8;
    cout <<"KiloByte To Bytes: "<<Bytes<<endl;
    cout <<"Bytes To Bits: "<<Bits<<endl;

    return 0;
}

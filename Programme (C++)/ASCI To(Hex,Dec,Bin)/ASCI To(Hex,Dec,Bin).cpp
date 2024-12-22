#include <iostream>
#include <bitset>
#include <iomanip>
using namespace std;

int main(){
    string ch;
    cout<<"Input Character One: ";
    cin>>ch;
    while (ch.length()!=1) {
        cout<<"Please input only one character: "<<endl;
        cin>>ch;
    }
    int chr=int(ch[0]);
    bitset<8> binary(chr);
    cout<<"Converted: "<<ch<<endl;
    cout<<"ASCII Value (Decimal): "<<chr<<endl;
    cout<<"ASCII Value (Hexadecimal): "<<hex<<chr<<endl;
    cout<<"ASCII Value (Binary): "<<binary<<endl;


    return 0;
}

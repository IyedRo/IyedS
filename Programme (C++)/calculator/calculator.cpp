#include <iostream>
using namespace std;

int main (){
    int a,b;
    string c;
    char r;


    cout<<"Input Number: ";
    cin>>a;
    cout<<"Input Number: ";
    cin>>b;
    cout<<"Choose('+','-','/','*'): ";
    cin>>r;

    if (r=='+') {
        cout<<a+b<<endl;
    } else if (r=='-'){
        cout<<a-b<<endl;
    } else if (r=='*'){
        cout<<a*b<<endl;
    } else if (r=='/'){
        if (b!=0){
            cout<<a/b<<endl;
        } else {
            cout<<"Error!"<<endl;
        }
    } else {
        cout<<"Invalid Input!"<<endl;
    }



    return 0;
}

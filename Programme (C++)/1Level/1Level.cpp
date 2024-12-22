#include <iostream>
using namespace std;

int main(){
    //Type Case
    cout<<"===================="<<endl;
    cout<<sizeof(int)<<endl;//4
    cout<<sizeof(float)<<endl;//4
    cout<<sizeof(double)<<endl;//8
    cout<<sizeof(string)<<endl;//32
    //Test
    cout<<"===================="<<endl;
    int num=10;
    num=20.5;//Update But Get Int Without Float
    cout<<num<<";"<<sizeof(num)<<endl;
    float nums=20.5;
    nums=10;//Update But Get Int Or Float
    cout<<nums<<";"<<sizeof(nums)<<endl;
    double dob=19.9;
    cout<<dob<<";"<<sizeof(dob)<<endl;
    float fl=10.5+9.5;
    cout<<fl<<";"<<sizeof(fl)<<endl;
    cout<<"===================="<<endl;
    char a='A';
    cout<<a<<";"<<int(a)<<endl;
    auto b='B';
    cout<<b<<";"<<int(b)<<endl;

    return 0;
}

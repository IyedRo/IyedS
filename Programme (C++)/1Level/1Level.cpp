#include <iostream>

int main()
{
    //Type Case
    std::cout<<"===================="<<std::endl;
    std::cout<<sizeof(int)<<std::endl;//4
    std::cout<<sizeof(float)<<std::endl;//4
    std::cout<<sizeof(double)<<std::endl;//8
    std::cout<<sizeof(std::string)<<std::endl;//32
    //Test
    std::cout<<"===================="<<std::endl;
    int num=10;
    num=20.5;//Update But Get Int Without Float
    std::cout<<num<<";"<<sizeof(num)<<std::endl;
    float nums=20.5;
    nums=10;//Update But Get Int Or Float
    std::cout<<nums<<";"<<sizeof(nums)<<std::endl;
    double dob=19.9;
    std::cout<<dob<<";"<<sizeof(dob)<<std::endl;
    float fl=10.5+9.5;
    std::cout<<fl<<";"<<sizeof(fl)<<std::endl;
    std::cout<<"===================="<<std::endl;
    char a='A';
    std::cout<<a<<";"<<int(a)<<std::endl;
    auto b='B';
    std::cout<<b<<";"<<int(b)<<std::endl;

    std::cout << "Press Enter to close...";
    std::cin.get();
    return 0;
}

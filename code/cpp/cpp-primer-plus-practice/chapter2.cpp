#include <iostream>
using namespace std;


// 2.7-1 print your name and location
void print_personal_info(){
    cout<<"Hi, Im Tina. I come from Australia."<<endl;
}

// 2.7-2 convert long to yd, 1 long = 220 yd
int convert_long_to_yd(int _long){
    int yd = _long * 220;
    cout<<_long<<" long = "<<yd<<" yard."<<endl;
    return yd;
}

// 2.7-3~7 no need.

int main(int argc, char const *argv[])
{
    // print_personal_info();
    // convert_long_to_yd(2);
    return 0;
}

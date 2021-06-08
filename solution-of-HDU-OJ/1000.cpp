#include <iostream>
using namespace std;

int main(){
    int a,b;
    while (cin>>a>>b){
    /*here 'cin>>a>>b' return the 'cin' obj., EOF or type error */
        cout<<a+b<<endl;
    }
    return 0;
}

#include <iostream>

int main(int argc, char const *argv[]){
    using namespace std;
    int number;
    while(cin >> number){
        int sum = 0;
        for (int i = 1; i <= number; ++i){
            sum += i;
        }
        cout<< sum << endl << endl;
    }
    return 0;
}

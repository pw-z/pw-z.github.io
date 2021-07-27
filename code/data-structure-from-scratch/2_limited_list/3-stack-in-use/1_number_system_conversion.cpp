/**
 * convert decimal to binary
 * decimal N = (N div d)*d + N mod d
 */

#include "stack.h"
#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    int decimal;
    while (1)
    {
        cout << "input a decimal: ";
        cin >> decimal;
        while (decimal)
        {
            stack.push(decimal % 2);
            decimal /= 2;
        }
        int i=0;
        cout<< "the binary is: ";
        while (!stack.isempty())
        {
            cout<<stack.pop();
            ++i;
            if(i%4 == 0 && i != 0)
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

/*
input a decimal: 16
the binary is: 1000 0
input a decimal: 1024
the binary is: 1000 0000 000
input a decimal: 3245234
the binary is: 1100 0110 0001 0010 1100 10
*/
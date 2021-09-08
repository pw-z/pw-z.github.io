#include "stack.h"
#include <iostream>

using std::cout;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    cout<<stack.length()<<std::endl;
    for (int i = 0; i < 100; i++)
    {
        stack.push(i);
    }
    cout<<stack.length()<<std::endl;
    cout<<stack.isempty()<<std::endl;
    cout<<stack.isfull()<<std::endl;
    stack.push(101);
    cout<<stack.pop()<<std::endl;
    
    return 0;
}

/*
0
100
0
1
expanded from 100 to 200
101
*/
#include "stack.h"
#include <iostream>

using std::cout;
using std::endl;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    cout<<"stack length is: "<<stack.length()<<endl;
    for (int i = 0; i < 10; i++)
    {
        stack.push(i);
    }
    cout<<"stack length is: "<<stack.length()<<endl;
    stack.push(101);
    cout<<"stack length is: "<<stack.length()<<endl;
    cout<<stack.pop()<<endl;
    while (stack.length()!=0)
    {
        cout<<stack.pop()<<endl;
    }
    // stack.suicide();
    cout<<"stack length is: "<<stack.length()<<endl;
    
    return 0;
}

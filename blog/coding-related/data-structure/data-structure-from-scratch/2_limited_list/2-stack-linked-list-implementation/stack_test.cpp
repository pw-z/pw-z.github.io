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

/*
p_base_ = 0x6d1e10
p_top_ = 0x401519
p_top_->next = 0x6d1e10
stack length is: 0
before push, p_top_ = 0x6d1e10  p_top_->next = 0x6d1e10
after  push, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
before push, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
after  push, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
before push, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
after  push, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
before push, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
after  push, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
before push, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
after  push, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
before push, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
after  push, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
before push, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
after  push, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
before push, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
after  push, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
before push, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
after  push, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
before push, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
after  push, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
stack length is: 10
before push, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
after  push, p_top_ = 0x6d41b0  p_top_->next = 0x6d4170
stack length is: 11
before pop, p_top_ = 0x6d41b0  p_top_->next = 0x6d4170
after  pop, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
101
before pop, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
after  pop, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
9
before pop, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
after  pop, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
8
before pop, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
after  pop, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
7
before pop, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
after  pop, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
6
before pop, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
after  pop, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
5
before pop, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
after  pop, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
4
before pop, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
after  pop, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
3
before pop, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
after  pop, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
2
before pop, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
after  pop, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
1
before pop, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
after  pop, p_top_ = 0x6d1e10  p_top_->next = 0x6d1e10
0
stack length is: 0
*/
#include "simulate_stack_using_two_queues.h"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    SimulateStack* stack = new SimulateStack();
    stack->push(1);
    stack->push(2);
    stack->push(3);
    cout<< stack->pop()<<endl;
    stack->push(4);
    stack->push(5);
    stack->push(6);
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    return 0;
}

/*
3
6
5
4
2
1
empty! pop failed.
0
*/


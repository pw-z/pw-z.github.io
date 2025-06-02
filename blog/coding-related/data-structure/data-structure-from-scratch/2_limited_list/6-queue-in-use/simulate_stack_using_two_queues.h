#include "queue.h"
#include <iostream>

using namespace std;

class SimulateStack
{
private:
    Queue<int>* q1;
    Queue<int>* q2;
    int length_;

public:
    SimulateStack();
    ~SimulateStack();
    int pop();
    bool push(int i);
};

SimulateStack::SimulateStack()
{
    q1 = new Queue<int>;
    q2 = new Queue<int>;
    length_ = 0;
}

SimulateStack::~SimulateStack()
{
    delete q1;
    delete q2;
}

bool SimulateStack::push(int i){
    q1->enqueue(i);
    length_ ++;
    return true;
}

int SimulateStack::pop(){
    if(length_ > 0){
        while (q1->length() > 1)
        {
            q2->enqueue(q1->dequeue());
        }
        int result = q1->dequeue();
        length_ --;

        while (q2->length() > 0)
        {
            q1->enqueue(q2->dequeue());
        }
        return result;
    }else{
        cout<<"empty! pop failed."<<endl;
        return NULL;
    }
}
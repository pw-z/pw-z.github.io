#ifndef QUEUE_H_
#define QUEUE_H_

#include <iostream>
using std::cout;
using std::cin;

static const int INIT_SIZE = 100;
static const int EXPAND_SIZE = 100;

template<class Item>
class Queue
{
private:
    Item* p_queue_;
    int capacity_;
    int length_;
public:
    Queue(/* args */);
    ~Queue();
    bool enqueue(Item e);
    Item dequeue();
    bool isempty();
    bool clear();
    int length();
};

template<class Item>
Queue<Item>::Queue(/* args */)
{
    p_queue_ = new Item[INIT_SIZE];
}

template<class Item>
Queue<Item>::~Queue()
{
    delete [] p_queue_;
}



#endif
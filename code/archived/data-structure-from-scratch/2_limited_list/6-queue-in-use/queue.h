#ifndef QUEUE_H_
#define QUEUE_H_

#include <iostream>
using std::cout;

static const int INIT_SIZE = 10;
static const int EXPAND_SIZE = 10;

template<class Item>
class Queue
{
private:
    Item* p_queue_;
    int capacity_;
    int length_;
    int head_;
    int tail_;
    bool expand(){
        Item* temp = new Item[capacity_ + EXPAND_SIZE];
        for (int i = 0; i < capacity_; i++)
        {
            temp[i] = p_queue_[i];
        }
        delete [] p_queue_;
        p_queue_ = temp;
        capacity_ += EXPAND_SIZE;
        std::cout << "expanded from " << capacity_ - EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    }
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
    capacity_ = INIT_SIZE;
    length_ = 0;
    head_ = 0;
    tail_ = 0;
}

template<class Item>
Queue<Item>::~Queue()
{
    delete [] p_queue_;
}

template<class Item>
bool Queue<Item>::enqueue(Item e)
{
    if(tail_ == capacity_){
        if(head_ != 0){
            //move items to the head of the queue, then consider expanding
            for (int i = 0; i < length_; i++)
            {
                p_queue_[i] = p_queue_[head_ + i];
            }
            head_ = 0;
            tail_ = length_;
        }else{  // length_ == capacity_
            if (!expand()){
                return false;
            }
        }
    }
    p_queue_[tail_] = e;
    length_++;
    tail_++;
    return true;
}

template<class Item>
Item Queue<Item>::dequeue()
{
    if (isempty())
    {
        cout << "!dequeue failed: an empty queue\n";
        return NULL;
    }
    Item e = p_queue_[head_];
    head_++;
    length_--;
    return e;   
}

template<class Item>
bool Queue<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
bool Queue<Item>::clear(){
    head_ = 0;
    tail_ = 0;
    length_ = 0;
}

template<class Item>
int Queue<Item>::length(){
    return length_;
}

#endif
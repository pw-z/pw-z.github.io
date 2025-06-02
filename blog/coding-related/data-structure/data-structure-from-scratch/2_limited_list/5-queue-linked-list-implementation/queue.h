#ifndef QUEUE_H_
#define QUEUE_H_

#include <iostream>
using std::cout;

template<class Item>
class Node{
public:
    Item data;
    Node* next;
};

template<class Item>
class Queue
{
private:
    Node<Item>* head;
    Node<Item>* tail;
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
    head = new Node<Item>;
    head->next = head;
    tail = head;
    length_ = 0;
}

template<class Item>
Queue<Item>::~Queue()
{
    clear();
}

template<class Item>
bool Queue<Item>::enqueue(Item e){
    tail->data = e;
    Node<Item>* temp = new Node<Item>;
    tail->next = temp;
    tail = temp;
    length_++;
    return true;
}

template<class Item>
Item Queue<Item>::dequeue(){
    if(isempty()){
        cout<< "!dequeue failed, an empty queue";
        return NULL;
    }
    Item e = head->data;
    Node<Item>* temp = head;
    head = head->next;
    delete temp;
    length_--;
    return e;
}

template<class Item>
bool Queue<Item>::clear(){
    Node<Item>* temp;
    while (length_ != 0)
    {
        temp = head;
        head = head->next;
        delete temp;
        length_--;
    }
    cout<<"head = " << head << "\n";
    cout<<"tail = " << tail << "\n";
    return true;
}

template<class Item>
bool Queue<Item>::isempty(){
    if (length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
int Queue<Item>::length(){
    return length_;
}

#endif
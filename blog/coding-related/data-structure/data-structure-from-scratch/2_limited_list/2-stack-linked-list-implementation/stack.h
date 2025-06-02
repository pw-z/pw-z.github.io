#ifndef STACK_H_
#define STACK_H_

#include <iostream>
using std::cout;
using std::endl;


template<class Item>
class Node{
public:
    Item data;
    Node* next;
};


template<class Item>
class Stack{
private:
    Node<Item>* p_base_;
    Node<Item>* p_top_;
    int length_;
    
public:
    Stack();
    ~Stack();
    Item pop();
    bool push(Item item);
    bool suicide();
    bool clear();
    bool isempty();
    // bool isfull();
    int length();
};

template<class Item>
Stack<Item>::Stack(){
    
    p_base_ = new Node<Item>;
    cout<<"p_base_ = "<<p_base_<<endl;
    cout<<"p_top_ = "<<p_top_<<endl;
    p_base_->next = p_base_;
    p_top_ = p_base_;
    cout<<"p_top_->next = "<<p_top_->next<<endl;
    length_ = 0;
}

template<class Item>
Stack<Item>::~Stack(){
    while (length_ != 0)
    {
        pop();
    }
    delete p_base_;
}

template<class Item>
bool Stack<Item>::suicide(){
    while (length_ != 0)
    {
        pop();
    }
    delete p_base_;
    return true;
}

template<class Item>
bool Stack<Item>::clear(){
    while (length_ != 0)
    {
        pop();
    }
    return true;
}

template<class Item>
bool Stack<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
bool Stack<Item>::push(Item e){
    cout<<"before push, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    Node<Item>* new_node = new Node<Item>;
    new_node->data = e;
    new_node->next = p_top_;
    p_top_ = new_node;
    ++length_;
    cout<<"after  push, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    return true;
}

template<class Item>
Item Stack<Item>::pop(){
    cout<<"before pop, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    if(length_ == 0){
        std::cout<<"!pop failed: an empty stack"<<std::endl;
        return 0;
    }
    Item e = p_top_->data;
    Node<Item>* temp = p_top_;
    p_top_ = p_top_->next;
    delete temp;
    --length_;
    cout<<"after  pop, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    return e;
}

template<class Item>
int Stack<Item>::length(){
    return length_;
}

#endif
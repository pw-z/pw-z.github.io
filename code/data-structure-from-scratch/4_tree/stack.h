#ifndef STACK_H_
#define STACK_H_

#include<cstring>
#include<iostream>

static const int INIT_SIZE = 100;
static const int EXPAND_SIZE = 100;

template<class Item>
class Stack
{
private:
    Item* p_stack_;
    int top_;
    int capacity_;
    int length_;
    bool expand(){
        Item* temp;
        try{
            temp = new Item[capacity_ + EXPAND_SIZE];
            memcpy(temp, p_stack_, length_ * sizeof(Item));
        }catch(std::bad_alloc e){
            std::cerr << e.what() << '\n';
            return false;
        }
        delete [] p_stack_;
        p_stack_ = temp;
        capacity_ += EXPAND_SIZE;
        std::cout << "expanded from " << capacity_ - EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    }
    
public:
    Stack();
    ~Stack();
    Item pop();
    bool push(Item item);
    bool suicide();
    bool clear();
    bool isempty();
    bool isfull();
    int length();
};

template<class Item>
Stack<Item>::Stack(){
    p_stack_ = new Item[INIT_SIZE];
    top_ = -1;
    capacity_ = INIT_SIZE;
    length_ = 0;
}

template<class Item>
Stack<Item>::~Stack(){
    delete [] p_stack_;
}

template<class Item>
bool Stack<Item>::push(Item item){
    if(isfull()){
        if(!expand()){
            return false;
        }
    }
    p_stack_[top_+1] = item;
    ++top_;
    ++length_;
    return true;
}

template<class Item>
Item Stack<Item>::pop(){
    if(isempty()){
        std::cout<<"!pop failed: an empty stack"<<std::endl;
        return NULL;  // ...
    }
    Item e = p_stack_[top_];
    --top_;
    --length_;
    return e;
}

template<class Item>
bool Stack<Item>::suicide(){
    delete [] p_stack_;
    return true;
}

template<class Item>
bool Stack<Item>::clear(){
    top_ = -1;
    length_ = 0;
    return true;
}

template<class Item>
bool Stack<Item>::isfull(){
    if(length_ == capacity_)
        return true;
    else
        return false;
}

template<class Item>
bool Stack<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
int Stack<Item>::length(){
    return length_;
}

#endif
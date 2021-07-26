#ifndef STACK_H_
#define STACK_H_

static const int INIT_SIZE = 100;
static const int EXPAND_SIZE = 100;

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
    
    Node<Item>* p_base_ = new Node<Item>;
    Node<Item>* p_top_;
    p_top_->next = p_base_;
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
    Node<Item>* new_node = new Node<Item>;
    new_node->data = e;
    new_node->next = p_top_;
    p_top_ = new_node;
    ++length_;
    return true;
}

template<class Item>
Item Stack<Item>::pop(){
    if(length_ == 0){
        return 0;
    }
    Item e = p_top_->data;
    Node<Item>* temp = p_top_;
    p_top_ = p_top_->next;
    delete temp;
    --length_;
    return e;
}

template<class Item>
int Stack<Item>::length(){
    return length_;
}

#endif
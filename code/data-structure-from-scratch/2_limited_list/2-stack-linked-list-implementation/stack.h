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
    bool isfull();
    int length();
};

template<class Item>
Stack<Item>::Stack(){
    length_ = 0;
}

#endif
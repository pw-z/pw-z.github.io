#ifndef STACK_H_
#define sTACK_H_
#include <string>

typedef std::string Item;

class Stack
{
private:
    enum {MAX = 10};
    Item items[MAX];
    int top;
public:
    Stack();
    bool isempty() const;
    bool isfull() const;
    bool push(const Item & item);
    Item pop();
};

#endif
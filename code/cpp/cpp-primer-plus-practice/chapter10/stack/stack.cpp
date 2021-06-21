#include "stack.h"

Stack::Stack(){
    top = 0;
}

bool Stack::isempty() const{
    return top == 0;
}

bool Stack::isfull() const { 
    return top == MAX;
}

bool Stack::push(const Item & item){
    if (top < MAX)
    {
        items[top++] = item;
        return true;
    }else{
        return false;
    }
}

Item Stack::pop(){
    if (top > 0)
    {
        return items[--top];
    }else
        return "Error";
}
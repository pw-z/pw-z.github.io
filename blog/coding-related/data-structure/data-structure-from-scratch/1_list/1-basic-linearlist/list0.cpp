#include "list0.h"
#include <iostream>

List::List() {
    _length = 0;
}

bool List::insert(int i, Item e) {
    if (i < 1 || i > _length + 1)
        return false;
    if (isfull())
        return false;
    for (int index = _length; index >= i; --index) {
        items[index] = items[index - 1];
    }
    items[i - 1] = e;
    ++_length;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > _length)
        return false;
    if (i == _length) {
        --_length;
        return true;
    }
    for (int index = i; index <= _length; ++index) {
        items[index - 1] = items[index];
    }
    --_length;
    return true;
}

bool List::replace(int i, Item e) {
    if (i<1 | i> _length)
        return false;
    items[i - 1] = e;
    return true;
}

Item List::get(int i) {
    if (i < 1 || i > _length) {
        std::cout << "Error: invalid index";
        // here must return something, but return what?
        Item e;
        return e;
    } else
        return items[i - 1];
}

int List::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < _length; ++i) {
        if (items[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {
    if (isempty()) {
        std::cout << "Error: try to print an empty list";
    } else {
        for (int i = 0; i < _length; i++) {
            std::cout << items[i] << " ";
        }
        std::cout<<"\n";
    }
}

int List::length() {
    return _length;
}

bool List::isempty() const {
    if (_length == 0) {
        return true;
    } else {
        return false;
    }
}

bool List::isfull() const {
    if (_length == MAX) {
        return true;
    } else {
        return false;
    }
}
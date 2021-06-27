#include "list1.h"
#include "list1_exception.h"
#include <iostream>

List::List() {
    _length = 0;
}

bool List::insert(int i, Item e) {
    if (i < 1 || i > _length + 1) {
        InvalidIndexException iie;
        throw iie;
    }
    if (isfull()) {
        FullListException fle;
        throw fle;
    }
    for (int index = _length; index >= i; --index) {
        items[index] = items[index - 1];
    }
    items[i - 1] = e;
    ++_length;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > _length) {
        InvalidIndexException iie;
        throw iie;
    }
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
    if (i<1 | i> _length) {
        InvalidIndexException iie;
        throw iie;
    }
    items[i - 1] = e;
    return true;
}

Item List::get(int i) {
    if (i < 1 || i > _length) {
        InvalidIndexException iie;
        throw iie;
    } else
        return items[i - 1];
}

int List::find(Item e) {
    if (isempty()) {
        return -1;
    }
    for (int i = 0; i < _length; ++i) {
        if (items[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {
    if (isempty()) {
        EmptyListException ele;
        throw ele;
    } else {
        for (int i = 0; i < _length; i++) {
            std::cout << items[i] << " ";
        }
        std::cout << "\n";
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
#include "list2.h"
#include <iostream>

List::List() {
    p_items_ = new Item[LIST_INIT_SIZE];
    capacity_ = LIST_INIT_SIZE;
    length_ = 0;
}

List::~List() {
    delete[] p_items_;
}

bool List::insert(int i, Item e) {  // updated
    if (isfull()) {
        if (!expand())
            return false;
    }
    for (int index = length_; index >= i; --index) {
        p_items_[index] = p_items_[index - 1];
    }
    p_items_[i - 1] = e;
    ++length_;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > length_)
        return false;
    if (i == length_) {
        --length_;
        return true;
    }
    for (int index = i; index <= length_; ++index) {
        p_items_[index - 1] = p_items_[index];
    }
    --length_;
    return true;
}

bool List::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    p_items_[i - 1] = e;
    return true;
}

bool List::get(int i, Item& e) {  // updated
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        e = p_items_[i - 1];
        return true;
    }
}

int List::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < length_; ++i) {
        if (p_items_[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {  // updated
    if (isempty()) {
        std::cout << "Error: try to print an empty list\n";
    } else {
        for (int i = 0; i < length_; i++) {
            if (i != 0 && i % 10 == 0)
                std::cout << "\n";
            std::cout << p_items_[i] << " ";
        }
        std::cout << "\n";
    }
}

int List::length() {
    return length_;
}

bool List::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

bool List::isfull() const {
    if (length_ == capacity_) {
        return true;
    } else {
        return false;
    }
}
#ifndef LINEARLIST_H_
#define LINEARLIST_H_


#include <cstring>
#include <iostream>

namespace linear {

static int LIST_INIT_SIZE = 100000;
static int LIST_EXPAND_SIZE = 100000;

// typedef int Item;
template<class Item>
class List {
   private:
    Item* p_items_;
    int capacity_;
    int length_;
    bool expand() {
        Item* temp;
        try {
            temp = new Item[capacity_ + LIST_EXPAND_SIZE];
            memcpy(temp, p_items_, length_ * sizeof(Item));
        } catch (std::bad_alloc e) {
            std::cout << "Error: allocate new memory failed.\n";
            std::cout << e.what();
            return false;
        }
        delete[] p_items_;
        p_items_ = temp;
        capacity_ += LIST_EXPAND_SIZE;
        // std::cout << "expanded from " << capacity_-LIST_EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    };

   public:
    List();
    ~List();  // new for `delete`
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);  // little change
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};


template<class Item>
List<Item>::List() {
    p_items_ = new Item[LIST_INIT_SIZE];
    capacity_ = LIST_INIT_SIZE;
    length_ = 0;
}

template<class Item>
List<Item>::~List() {
    delete[] p_items_;
}

template<class Item>
bool List<Item>::insert(int i, Item e) {  // updated
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

template<class Item>
bool List<Item>::remove(int i) {
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

template<class Item>
bool List<Item>::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    p_items_[i - 1] = e;
    return true;
}

template<class Item>
bool List<Item>::get(int i, Item& e) {  // updated
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        e = p_items_[i - 1];
        return true;
    }
}

template<class Item>
int List<Item>::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < length_; ++i) {
        if (p_items_[i] == e)
            return i + 1;
    }
    return -1;
}

template<class Item>
void List<Item>::printlist() const {  // updated
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

template<class Item>
int List<Item>::length() {
    return length_;
}

template<class Item>
bool List<Item>::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

template<class Item>
bool List<Item>::isfull() const {
    if (length_ == capacity_) {
        return true;
    } else {
        return false;
    }
}

}  // namespace

#endif
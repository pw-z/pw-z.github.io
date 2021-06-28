#ifndef LIST4_H_
#define LIST4_H_

#include <cstring>
#include <iostream>

static int LIST_INIT_SIZE = 10;
static int LIST_EXPAND_SIZE = 10;

template <class Item>
class Node {
   public:
    Item item;
    Item* next;
};

template <class Item>
class List {
   private:
    Node<Item>* head;
    int length_;

   public:
    List();
    ~List();
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};

template <class Item>
List<Item>::List() {
    head = new Node<Item>;
    head->item = 999;
    std::cout<<"head location: " << head << "\n";
    length_ = 0;
}

template <class Item>
List<Item>::~List() {
    // for item in length, delete node->next
    std::cout<<"head item: " << head->item<<"\n";
    delete head;
}

// template <class Item>
// bool List<Item>::insert(int i, Item e) {
//     if (i < 1 || i > length_ + 1)
//         return false;

//     ++length_;
//     return true;
// }

// template <class Item>
// bool List<Item>::remove(int i) {
//     if (i < 1 || i > length_)
//         return false;
//     if (i == length_) {
//         --length_;
//         return true;
//     }
//     for (int index = i; index <= length_; ++index) {
//         p_items_[index - 1] = p_items_[index];
//     }
//     --length_;
//     return true;
// }

// template <class Item>
// bool List<Item>::replace(int i, Item e) {
//     if (i<1 | i> length_)
//         return false;
//     p_items_[i - 1] = e;
//     return true;
// }

// template <class Item>
// bool List<Item>::get(int i, Item& e) {
//     if (i < 1 || i > length_) {
//         std::cout << "Error: invalid index\n";
//         // here must return something
//         return false;
//     } else {
//         e = p_items_[i - 1];
//         return true;
//     }
// }

// template <class Item>
// int List<Item>::find(Item e) {
//     if (isempty())
//         return -1;
//     for (int i = 0; i < length_; ++i) {
//         if (p_items_[i] == e)
//             return i + 1;
//     }
//     return -1;
// }

// template <class Item>
// void List<Item>::printlist() const {  // updated
//     if (isempty()) {
//         std::cout << "Error: try to print an empty list\n";
//     } else {
//         for (int i = 0; i < length_; i++) {
//             if (i != 0 && i % 10 == 0)
//                 std::cout << "\n";
//             std::cout << p_items_[i] << " ";
//         }
//         std::cout << "\n";
//     }
// }

// template <class Item>
// int List<Item>::length() {
//     return length_;
// }

// template <class Item>
// bool List<Item>::isempty() const {
//     if (length_ == 0) {
//         return true;
//     } else {
//         return false;
//     }
// }

// template <class Item>
// bool List<Item>::isfull() const {
//     if (length_ == capacity_) {
//         return true;
//     } else {
//         return false;
//     }
// }
#endif
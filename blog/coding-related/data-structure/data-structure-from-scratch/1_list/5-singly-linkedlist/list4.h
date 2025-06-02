#ifndef LIST4_H_
#define LIST4_H_

#include <cstring>
#include <iostream>

template <class Item>
class Node {
   public:
    Item item;
    Node* next;
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
    // bool isfull() const;
};

template <class Item>
List<Item>::List() {
    head = new Node<Item>;
    head->next = NULL;
    // std::cout<<"head location: " << head << "\n";
    length_ = 0;
}

template <class Item>
List<Item>::~List() {
    // for item in length, delete node->next
    Node<Item>* p = head->next;
    while (p != NULL) {
        Node<Item>* q = p;
        p = p->next;
        delete q;
    }
    delete head;
}

template <class Item>
bool List<Item>::insert(int i, Item e) {
    if (i < 1 || i > length_ + 1)
        return false;

    Node<Item>* p = head;
    while (--i) {
        p = p->next;
    }

    Node<Item> * node = new Node<Item>();
    node->item = e;
    node->next = p->next;
    p->next = node;

    ++length_;
    return true;
}

template <class Item>
bool List<Item>::remove(int i) {
    if (i < 1 || i > length_)
        return false;
    
    Node<Item>* p = head;
    Node<Item>* temp;
    while (--i)
    {
        p = p->next;
    }
    temp = p->next;
    p->next = temp->next;
    delete temp;
    --length_;

    return true;
}

template <class Item>
bool List<Item>::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    
    Node<Item>* p = head;
    while (i--)
    {
        p = p->next;
    }
    p->item = e;
    
    return true;
}

template <class Item>
bool List<Item>::get(int i, Item& e) {
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        Node<Item>* p = head;
        while (i--) {
            p = p->next;
        }
        e = p->item;
        
        return true;
    }
}

template <class Item>
int List<Item>::find(Item e) {
    if (isempty())
        return -1;
    Node<Item>* p = head->next;
    int index = 0;
    while (p !=NULL)
    {   
        ++index;
        if (p->item == e)
        {
            return index;
        }
        p = p->next;
    }
    return -1;
}

template <class Item>
void List<Item>::printlist() const {  // updated
    if (isempty()) {
        std::cout << "Error: try to print an empty list\n";
    } else {
        Node<Item>* p = head->next;
        int count = 0;
        while (p != NULL) {
            std::cout << p->item << " ";
            p = p->next;
            ++count;
            if (count % 10 == 0 && count != 0)
            {
                std::cout<<"\n";
            }
            
        }
        std::cout << "\n";
    }
}

template <class Item>
int List<Item>::length() {
    return length_;
}

template <class Item>
bool List<Item>::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

// template <class Item>
// bool List<Item>::isfull() const {
//     if (length_ == capacity_) {
//         return true;
//     } else {
//         return false;
//     }
// }

#endif
#ifndef LIST2_H_
#define LIST2_H_

#include <cstring>
#include <iostream>
typedef int Item;

static int LIST_INIT_SIZE = 10;
static int LIST_EXPAND_SIZE = 10;

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
        std::cout << "expanded from " << capacity_-LIST_EXPAND_SIZE << " to " << capacity_ << "\n";
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

#endif
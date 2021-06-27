#ifndef LIST0_H_
#define LIST0_H_

typedef int Item;

class List
{
private:
    int INIT_SIZE = 10;
    Item * p_items;
    int _length;
public:
    List();
    ~List();
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    Item get(int i);
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};

#endif
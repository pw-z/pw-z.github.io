#ifndef LIST0_H_
#define LIST0_H_

typedef int Item;

class List
{
private:
    enum {MAX = 100};
    Item items[MAX];
public:
    List();
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    Item get(int i);
    int find(Item e);
    void printlist();
    void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};

List::List(/* args */)
{
    
}

#endif
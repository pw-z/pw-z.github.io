#ifndef LIST1_H_
#define LIST1_H_

typedef int Item;

class List
{
private:
    enum {MAX = 100};
    Item items[MAX];
    int _length;
public:
    List();
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
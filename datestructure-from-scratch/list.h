typedef int Item;

class List
{
private:
    enum {MAX = 10};
    Item items[MAX];
public:
    List();
    bool insert(int i, Item e);
    bool remove(int i);
    
    bool isempty() const;
    bool isfull() const;
};

List::List(/* args */)
{
}
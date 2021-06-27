#include <iostream>
#include "list2.h"

using namespace std;

int main(int argc, char const* argv[]) {
    List mylist = List();
    cout << mylist.isempty() << endl;
    mylist.insert(1, 1);
    cout << mylist.isempty() << endl;
    mylist.insert(1, 2);
    mylist.insert(3, 3);
    mylist.printlist();
    mylist.insert(4, 4);
    mylist.printlist();
    for (int i = 0; i < 96; i++) {
        mylist.insert(1, i + 5);
    }
    mylist.printlist();
    mylist.insert(1, 9999);
    cout << mylist.isfull() << endl;
    mylist.remove(1);
    cout << mylist.isfull() << endl;
    mylist.printlist();
    mylist.replace(1, 2087);
    cout << mylist.get(1) << endl;
    int index = mylist.find(2087);
    cout << "find 2087 at " << index << endl;
    cout << mylist.length() << endl;

    return 0;
}

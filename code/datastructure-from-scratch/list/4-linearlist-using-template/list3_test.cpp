#include "list2.h"
#include <iostream>

using namespace std;

int main(int argc, char const* argv[]) {
    List mylist = List();
    cout << "current list length = " << mylist.length() << endl;
    mylist.printlist();
    for (int i = 0; i < 21; i++) {
        mylist.insert(1, 1);
        // cout << "current list length = " << mylist.length() << endl;
        // mylist.printlist();
    }
    cout << "current list length = " << mylist.length() << endl;
    mylist.printlist();
    mylist.replace(8, 8);
    mylist.replace(20, 20);
    mylist.remove(21);
    cout << "current list length = " << mylist.length() << endl;
    mylist.printlist();
    cout << "find 8 in list at " << mylist.find(8) << endl;
    cout << "find 20 in list at " << mylist.find(20) << endl;
    Item myitem;
    mylist.get(8, myitem);
    cout << "get item >>" << myitem << "<< from list" << endl;
    return 0;
}

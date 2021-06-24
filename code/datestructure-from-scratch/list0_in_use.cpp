#include "list0.h"
#include <iostream>

using namespace std;



int main(int argc, char const *argv[])
{
    List mylist = List();
    cout << mylist.isempty() << endl;
    mylist.insert(1, 19);
    cout << mylist.isempty() << endl;
    mylist.insert(1, 11);
    mylist.insert(3, 123);
    mylist.printlist();
    return 0;
}

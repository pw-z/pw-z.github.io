#include "list4.h"
#include <iostream>

int main(int argc, char const *argv[])
{
    using std::cout;

    List<int> mylist = List<int>();
    mylist.printlist();
    mylist.insert(1, 4);
    mylist.printlist();
    return 0;
}

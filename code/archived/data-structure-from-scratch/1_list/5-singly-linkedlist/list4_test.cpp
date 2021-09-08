#include "list4.h"
#include <iostream>

using namespace std;

int main(int argc, char const* argv[]) {

    List<int> mylist = List<int>();
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
    int myitem1;
    mylist.get(8, myitem1);
    cout << "get item '" << myitem1 << "' at 8 "<< endl;
    mylist.get(20, myitem1);
    cout << "get item '" << myitem1 << "' at 20 "<< endl;
    
    cout<<"\n\n\n";

    List<char> mylist2;
    cout << "current list length = " << mylist2.length() << endl;
    mylist2.printlist();
    for (int i = 0; i < 21; i++) {
        mylist2.insert(1, '#');
        // cout << "current list length = " << mylist.length() << endl;
        // mylist.printlist();
    }
    cout << "current list length = " << mylist2.length() << endl;
    mylist2.printlist();
    mylist2.replace(8, '*');
    mylist2.replace(20, '$');
    mylist2.remove(21);
    cout << "current list length = " << mylist2.length() << endl;
    mylist2.printlist();
    cout << "find '*' in list at " << mylist2.find('*') << endl;
    cout << "find '$' in list at " << mylist2.find('$') << endl;
    char myitem2;
    mylist2.get(8, myitem2);
    cout << "get item '" << myitem2 << "' at 8 "<< endl;
    mylist2.get(20, myitem2);
    cout << "get item '" << myitem2 << "' at 20 "<< endl;
    return 0;
}
/*
$ ./a
current list length = 0
Error: try to print an empty list
current list length = 21
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1
current list length = 20
1 1 1 1 1 1 1 8 1 1
1 1 1 1 1 1 1 1 1 20

find 8 in list at 8
find 20 in list at 20
get item '8' at 8
get item '20' at 20



current list length = 0
Error: try to print an empty list
current list length = 21
# # # # # # # # # #
# # # # # # # # # #
#
current list length = 20
# # # # # # # * # #
# # # # # # # # # $

find '*' in list at 8
find '$' in list at 20
get item '*' at 8
get item '$' at 20

*/

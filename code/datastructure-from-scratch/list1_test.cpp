#include "list1.h"
#include <iostream>
#include "list1_exception.h"

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
    // mylist.insert(1, 9999);
    cout << mylist.isfull() << endl;
    mylist.remove(1);
    cout << mylist.isfull() << endl;
    mylist.printlist();
    mylist.replace(1, 2087);
    cout << mylist.get(1) << endl;
    int index = mylist.find(2087);
    cout << "find 2087 at " << index << endl;
    cout << mylist.length() << endl;

    // test Exception
    try {
        mylist.remove(199);
    } catch (InvalidIndexException e) {
        cout << e.msg << endl;
    }

    try {
        mylist.insert(1, 0);
        mylist.insert(1, 0);
    } catch (FullListException e) {
        cout << e.msg << endl;
    }

    try {
        mylist.printlist();
        // for (int i = 0; i < mylist.length();) { // here is a BUG!
        //     cout << "i = " << i << endl;
        //     mylist.remove(1);
        //     i++;
        // }
        for (int i = 0, len = mylist.length(); i < len; i++) {
            mylist.remove(1);
        }
        mylist.printlist();

    } catch (EmptyListException e) {
        cout << e.msg << endl;
    }

    return 0;
}
/*
$ ./a.exe
1
0
2 1 3
2 1 3 4
100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 2 1 3 4
1
0
99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 2 1 3 4
2087
find 2087 at 1
99
The index is invalid!
This list is FULL!
0 2087 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 2 1 3 4
This is an empty list!
*/
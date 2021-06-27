# Data Structure from Scratch: LinearList & Linkedlist

- [Data Structure from Scratch: LinearList & Linkedlist](#data-structure-from-scratch-linearlist--linkedlist)
  - [1 LinearList & Linkedlist from Scratch](#1-linearlist--linkedlist-from-scratch)
    - [1.1 Basic LinearList](#11-basic-linearlist)
      - [1.1.1 header](#111-header)
      - [1.1.2 implement](#112-implement)
      - [1.1.3 test](#113-test)
    - [1.2 LinearList with Error Handling](#12-linearlist-with-error-handling)
      - [1.2.1 exception class](#121-exception-class)
      - [1.2.2 header & implement](#122-header--implement)
      - [1.2.3 test](#123-test)
    - [1.3](#13)

## 1 LinearList & Linkedlist from Scratch

### 1.1 Basic LinearList

#### 1.1.1 header

```c++
// list0.h
#ifndef LIST0_H_
#define LIST0_H_

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
```

#### 1.1.2 implement

```c++
// list0.cpp
#include "list0.h"
#include <iostream>

List::List() {
    _length = 0;
}

bool List::insert(int i, Item e) {
    if (i < 1 || i > _length + 1)
        return false;
    if (isfull())
        return false;
    for (int index = _length; index >= i; --index) {
        items[index] = items[index - 1];
    }
    items[i - 1] = e;
    ++_length;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > _length)
        return false;
    if (i == _length) {
        --_length;
        return true;
    }
    for (int index = i; index <= _length; ++index) {
        items[index - 1] = items[index];
    }
    --_length;
    return true;
}

bool List::replace(int i, Item e) {
    if (i<1 | i> _length)
        return false;
    items[i - 1] = e;
    return true;
}

Item List::get(int i) {
    if (i < 1 || i > _length) {
        std::cout << "Error: invalid index";
        // here must return something, but return what?
        Item e;
        return e;
    } else
        return items[i - 1];
}

int List::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < _length; ++i) {
        if (items[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {
    if (isempty()) {
        std::cout << "Error: try to print an empty list";
    } else {
        for (int i = 0; i < _length; i++) {
            std::cout << items[i] << " ";
        }
        std::cout<<"\n";
    }
}

int List::length() {
    return _length;
}

bool List::isempty() const {
    if (_length == 0) {
        return true;
    } else {
        return false;
    }
}

bool List::isfull() const {
    if (_length == MAX) {
        return true;
    } else {
        return false;
    }
}
```

#### 1.1.3 test

```c++
// list0_test.cpp
#include <iostream>
#include "list0.h"

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

*/
```

### 1.2 LinearList with Error Handling

About C++ Exceptions and Error Handling, these pages hava some useful info: 
  * [C++ Super-FAQ : Exceptions and Error Handling](https://isocpp.org/wiki/faq/exceptions)
  * [对使用 C++ 异常处理应具有怎样的态度？ - 吴咏炜的回答 - 知乎](https://www.zhihu.com/question/22889420/answer/282031257)

Have a try anyway.

#### 1.2.1 exception class

Create some exception first:

```c++
#ifndef LIST1_EXCEPTION_H_
#define LIST1_EXCEPTION_H_

#include <string>

class InvalidIndexException {
   public:
    std::string msg = "The index is invalid!";
};

class EmptyListException {
   public:
    std::string msg = "This is an empty list!";
};

class FullListException {
   public:
    std::string msg = "This list is FULL!";
};
#endif
```

#### 1.2.2 header & implement

Just rename list0.h to list1.h, no content change of header.

```c++
// list1.cpp
#include "list1.h"
#include "list1_exception.h"
#include <iostream>

List::List() {
    _length = 0;
}

bool List::insert(int i, Item e) {
    if (i < 1 || i > _length + 1) {
        InvalidIndexException iie;
        throw iie;
    }
    if (isfull()) {
        FullListException fle;
        throw fle;
    }
    for (int index = _length; index >= i; --index) {
        items[index] = items[index - 1];
    }
    items[i - 1] = e;
    ++_length;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > _length) {
        InvalidIndexException iie;
        throw iie;
    }
    if (i == _length) {
        --_length;
        return true;
    }
    for (int index = i; index <= _length; ++index) {
        items[index - 1] = items[index];
    }
    --_length;
    return true;
}

bool List::replace(int i, Item e) {
    if (i<1 | i> _length) {
        InvalidIndexException iie;
        throw iie;
    }
    items[i - 1] = e;
    return true;
}

Item List::get(int i) {
    if (i < 1 || i > _length) {
        InvalidIndexException iie;
        throw iie;
    } else
        return items[i - 1];
}

int List::find(Item e) {
    if (isempty()) {
        return -1;
    }
    for (int i = 0; i < _length; ++i) {
        if (items[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {
    if (isempty()) {
        EmptyListException ele;
        throw ele;
    } else {
        for (int i = 0; i < _length; i++) {
            std::cout << items[i] << " ";
        }
        std::cout << "\n";
    }
}

int List::length() {
    return _length;
}

bool List::isempty() const {
    if (_length == 0) {
        return true;
    } else {
        return false;
    }
}

bool List::isfull() const {
    if (_length == MAX) {
        return true;
    } else {
        return false;
    }
}
```

#### 1.2.3 test

```c++
// list1_test.cpp
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
```

### 1.3 Dynamic Memory Version

#### 1.3.1 header
#### 1.3.2 implement
#### 1.3.3 test
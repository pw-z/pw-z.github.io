# Data Structure from Scratch: LinearList & Linkedlist

*Posted on 2021.07.05 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 


- [Data Structure from Scratch: LinearList \& Linkedlist](#data-structure-from-scratch-linearlist--linkedlist)
  - [1 List in C++](#1-list-in-c)
    - [1.1 Basic LinearList](#11-basic-linearlist)
      - [1.1.1 Header](#111-header)
      - [1.1.2 Implement](#112-implement)
      - [1.1.3 Test](#113-test)
    - [1.2 LinearList with Error Handling](#12-linearlist-with-error-handling)
      - [1.2.1 Exception Class](#121-exception-class)
      - [1.2.2 Header \& Implement](#122-header--implement)
      - [1.2.3 Test](#123-test)
    - [1.3 LinearList Dynamic Memory Version](#13-linearlist-dynamic-memory-version)
      - [1.3.1 Header](#131-header)
      - [1.3.2 Implement](#132-implement)
      - [1.3.3 Test](#133-test)
    - [1.4 LinearList Using Template Version](#14-linearlist-using-template-version)
      - [1.4.1 Header \& Implement](#141-header--implement)
      - [1.4.2 Test](#142-test)
    - [1.5 Singly LinkedList](#15-singly-linkedlist)
      - [1.5.1 Header \& Implement](#151-header--implement)
      - [1.5.2 Test](#152-test)
  - [2 LinkedList in Python3](#2-linkedlist-in-python3)
    - [2.1 Implement](#21-implement)
    - [2.2 Test](#22-test)
  - [3 Performance](#3-performance)
    - [3.1 LinearList vs LinkedList](#31-linearlist-vs-linkedlist)
    - [3.2 Performance Test](#32-performance-test)
      - [3.2.1 LINEARLIST\_H\_](#321-linearlist_h_)
      - [3.2.2 LINKEDLIST\_H\_](#322-linkedlist_h_)
      - [3.2.3 Test Code and Result](#323-test-code-and-result)
      - [3.2.4 Result Analysis](#324-result-analysis)


In order to review the data structure konwledge, I am going to implement the basic data structure from scratch using c++ or python, including linear & linked list, stack & queue, tree & binary tree, maybe something else. This is the first post, List.

## 1 List in C++

### 1.1 Basic LinearList

#### 1.1.1 Header

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

This list can only store `int` type value.

#### 1.1.2 Implement

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

#### 1.1.3 Test

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

#### 1.2.1 Exception Class

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

#### 1.2.2 Header & Implement

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

#### 1.2.3 Test

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

### 1.3 LinearList Dynamic Memory Version

#### 1.3.1 Header

```c++
// list2.h
#ifndef LIST2_H_
#define LIST2_H_

#include <cstring>
#include <iostream>
typedef int Item;

static int LIST_INIT_SIZE = 10;
static int LIST_EXPAND_SIZE = 10;

class List {
   private:
    Item* p_items_;
    int capacity_;
    int length_;
    bool expand() {
        Item* temp;
        try {
            temp = new Item[capacity_ + LIST_EXPAND_SIZE];
            memcpy(temp, p_items_, length_ * sizeof(Item));
        } catch (std::bad_alloc e) {
            std::cout << "Error: allocate new memory failed.\n";
            std::cout << e.what();
            return false;
        }
        delete[] p_items_;
        p_items_ = temp;
        capacity_ += LIST_EXPAND_SIZE;
        std::cout << "expanded from " << capacity_-LIST_EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    };

   public:
    List();
    ~List();  // new for `delete`
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);  // little change
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};

#endif
```
#### 1.3.2 Implement

```c++
// list2.cpp
#include "list2.h"
#include <iostream>

List::List() {
    p_items_ = new Item[LIST_INIT_SIZE];
    capacity_ = LIST_INIT_SIZE;
    length_ = 0;
}

List::~List() {
    delete[] p_items_;
}

bool List::insert(int i, Item e) {  // updated
    if (isfull()) {
        if (!expand())
            return false;
    }
    for (int index = length_; index >= i; --index) {
        p_items_[index] = p_items_[index - 1];
    }
    p_items_[i - 1] = e;
    ++length_;
    return true;
}

bool List::remove(int i) {
    if (i < 1 || i > length_)
        return false;
    if (i == length_) {
        --length_;
        return true;
    }
    for (int index = i; index <= length_; ++index) {
        p_items_[index - 1] = p_items_[index];
    }
    --length_;
    return true;
}

bool List::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    p_items_[i - 1] = e;
    return true;
}

bool List::get(int i, Item& e) {  // updated
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        e = p_items_[i - 1];
        return true;
    }
}

int List::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < length_; ++i) {
        if (p_items_[i] == e)
            return i + 1;
    }
    return -1;
}

void List::printlist() const {  // updated
    if (isempty()) {
        std::cout << "Error: try to print an empty list\n";
    } else {
        for (int i = 0; i < length_; i++) {
            if (i != 0 && i % 10 == 0)
                std::cout << "\n";
            std::cout << p_items_[i] << " ";
        }
        std::cout << "\n";
    }
}

int List::length() {
    return length_;
}

bool List::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

bool List::isfull() const {
    if (length_ == capacity_) {
        return true;
    } else {
        return false;
    }
}
```

#### 1.3.3 Test

```c++
// list2_test.cpp
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
/*
$ ./a.exe
current list length = 0
Error: try to print an empty list
expanded from 10 to 20
expanded from 20 to 30
current list length = 21
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1
current list length = 20
1 1 1 1 1 1 1 8 1 1
1 1 1 1 1 1 1 1 1 20
find 8 in list at 8
find 20 in list at 20
get item >>8<< from list
*/
```


### 1.4 LinearList Using Template Version

#### 1.4.1 Header & Implement

```c++
// list3.h
#ifndef LIST3_H_
#define LIST3_H_

#include <cstring>
#include <iostream>

static int LIST_INIT_SIZE = 10;
static int LIST_EXPAND_SIZE = 10;

// typedef int Item;
template<class Item>
class List {
   private:
    Item* p_items_;
    int capacity_;
    int length_;
    bool expand() {
        Item* temp;
        try {
            temp = new Item[capacity_ + LIST_EXPAND_SIZE];
            memcpy(temp, p_items_, length_ * sizeof(Item));
        } catch (std::bad_alloc e) {
            std::cout << "Error: allocate new memory failed.\n";
            std::cout << e.what();
            return false;
        }
        delete[] p_items_;
        p_items_ = temp;
        capacity_ += LIST_EXPAND_SIZE;
        std::cout << "expanded from " << capacity_-LIST_EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    };

   public:
    List();
    ~List();  // new for `delete`
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);  // little change
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};


template<class Item>
List<Item>::List() {
    p_items_ = new Item[LIST_INIT_SIZE];
    capacity_ = LIST_INIT_SIZE;
    length_ = 0;
}

template<class Item>
List<Item>::~List() {
    delete[] p_items_;
}

template<class Item>
bool List<Item>::insert(int i, Item e) {  // updated
    if (isfull()) {
        if (!expand())
            return false;
    }
    for (int index = length_; index >= i; --index) {
        p_items_[index] = p_items_[index - 1];
    }
    p_items_[i - 1] = e;
    ++length_;
    return true;
}

template<class Item>
bool List<Item>::remove(int i) {
    if (i < 1 || i > length_)
        return false;
    if (i == length_) {
        --length_;
        return true;
    }
    for (int index = i; index <= length_; ++index) {
        p_items_[index - 1] = p_items_[index];
    }
    --length_;
    return true;
}

template<class Item>
bool List<Item>::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    p_items_[i - 1] = e;
    return true;
}

template<class Item>
bool List<Item>::get(int i, Item& e) {  // updated
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        e = p_items_[i - 1];
        return true;
    }
}

template<class Item>
int List<Item>::find(Item e) {
    if (isempty())
        return -1;
    for (int i = 0; i < length_; ++i) {
        if (p_items_[i] == e)
            return i + 1;
    }
    return -1;
}

template<class Item>
void List<Item>::printlist() const {  // updated
    if (isempty()) {
        std::cout << "Error: try to print an empty list\n";
    } else {
        for (int i = 0; i < length_; i++) {
            if (i != 0 && i % 10 == 0)
                std::cout << "\n";
            std::cout << p_items_[i] << " ";
        }
        std::cout << "\n";
    }
}

template<class Item>
int List<Item>::length() {
    return length_;
}

template<class Item>
bool List<Item>::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

template<class Item>
bool List<Item>::isfull() const {
    if (length_ == capacity_) {
        return true;
    } else {
        return false;
    }
}
#endif
```

#### 1.4.2 Test

```c++
// list3_test.cpp
#include "list3.h"
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
$ ./a.exe
current list length = 0
Error: try to print an empty list
expanded from 10 to 20
expanded from 20 to 30
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
expanded from 10 to 20
expanded from 20 to 30
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
```


### 1.5 Singly LinkedList

#### 1.5.1 Header & Implement

```c++
// list4.h
#ifndef LIST4_H_
#define LIST4_H_

#include <cstring>
#include <iostream>

static int LIST_INIT_SIZE = 10;
static int LIST_EXPAND_SIZE = 10;

template <class Item>
class Node {
   public:
    Item item;
    Node* next;
};

template <class Item>
class List {
   private:
    Node<Item>* head;
    int length_;

   public:
    List();
    ~List();
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    // bool isfull() const;
};

template <class Item>
List<Item>::List() {
    head = new Node<Item>;
    head->next = NULL;
    // std::cout<<"head location: " << head << "\n";
    length_ = 0;
}

template <class Item>
List<Item>::~List() {
    // for item in length, delete node->next
    Node<Item>* p = head->next;
    while (p != NULL) {
        Node<Item>* q = p;
        p = p->next;
        delete q;
    }
    delete head;
}

template <class Item>
bool List<Item>::insert(int i, Item e) {
    if (i < 1 || i > length_ + 1)
        return false;

    Node<Item>* p = head;
    while (--i) {
        p = p->next;
    }

    Node<Item> * node = new Node<Item>();
    node->item = e;
    node->next = p->next;
    p->next = node;

    ++length_;
    return true;
}

template <class Item>
bool List<Item>::remove(int i) {
    if (i < 1 || i > length_)
        return false;
    
    Node<Item>* p = head;
    Node<Item>* temp;
    while (--i)
    {
        p = p->next;
    }
    temp = p->next;
    p->next = temp->next;
    delete temp;
    --length_;

    return true;
}

template <class Item>
bool List<Item>::replace(int i, Item e) {
    if (i<1 | i> length_)
        return false;
    
    Node<Item>* p = head;
    while (i--)
    {
        p = p->next;
    }
    p->item = e;
    
    return true;
}

template <class Item>
bool List<Item>::get(int i, Item& e) {
    if (i < 1 || i > length_) {
        std::cout << "Error: invalid index\n";
        // here must return something
        return false;
    } else {
        Node<Item>* p = head;
        while (i--) {
            p = p->next;
        }
        e = p->item;
        
        return true;
    }
}

template <class Item>
int List<Item>::find(Item e) {
    if (isempty())
        return -1;
    Node<Item>* p = head->next;
    int index = 0;
    while (p !=NULL)
    {   
        ++index;
        if (p->item == e)
        {
            return index;
        }
        p = p->next;
    }
    return -1;
}

template <class Item>
void List<Item>::printlist() const {  // updated
    if (isempty()) {
        std::cout << "Error: try to print an empty list\n";
    } else {
        Node<Item>* p = head->next;
        int count = 0;
        while (p != NULL) {
            std::cout << p->item << " ";
            p = p->next;
            ++count;
            if (count % 10 == 0 && count != 0)
            {
                std::cout<<"\n";
            }
            
        }
        std::cout << "\n";
    }
}

template <class Item>
int List<Item>::length() {
    return length_;
}

template <class Item>
bool List<Item>::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

// template <class Item>
// bool List<Item>::isfull() const {
//     if (length_ == capacity_) {
//         return true;
//     } else {
//         return false;
//     }
// }

#endif
```

#### 1.5.2 Test

```c++
// list4_test.cpp
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
```

## 2 LinkedList in Python3

### 2.1 Implement

```python
# linkedlist.py
class LinkedList(object):

    class __Node(object):
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.__head = self.__Node(None)
        self.__head.next = None
        self.__length = 0

    def insert(self, index, value):
        if index > self.__length+1 or index < 1:
            raise IndexError

        node = self.__Node(value)
        if self.__length == 0:  # index == 1
            self.__head.next = node
            self.__length += 1
            return True

        p = self.__head
        for i in range(index-1):
            p = p.next

        node.next = p.next
        p.next = node
        self.__length += 1
        return True

    def print_list(self):
        p = self.__head
        count = 0
        while p.next is not None and count <= self.__length:
            p = p.next
            if count != 0 and count % 10 == 0:
                print()
            print(p.item, end=' ')
            count += 1
        print()

    def remove(self, index):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index - 1):
            p = p.next
        p.next = p.next.next
        return True

    def replace(self, index, value):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index):
            p = p.next
        p.item = value
        return True

    def get(self, index):
        if index > self.__length or index < 1:
            raise IndexError
        p = self.__head
        for i in range(index):
            p = p.next
        return p.item

    def find(self, value):
        p = self.__head
        count = 0
        while p.next is not None:
            p = p.next
            count += 1
            if p.item is value:
                return count
        return -1

    def length(self):
        return self.__length

```

### 2.2 Test

```python
if __name__ == '__main__':
    li = LinkedList()
    for i in range(20):
        li.insert(i+1, i+1)
        # print(i)
    li.print_list()
    li.insert(21, 999)

    # li.insert(50, 8989879)
    li.print_list()
    li.remove(21)
    li.print_list()
    li.replace(10, 77)
    li.print_list()
    print(li.get(10))
    print(li.find(77))
    print(li.length())

    print('='*30)

    s_li = LinkedList()
    for i in range(20):
        s_li.insert(i+1, '*')
    s_li.print_list()
    s_li.insert(10, '&')
    s_li.insert(15, '$')
    s_li.print_list()
    s_li.replace(22, '@')
    s_li.print_list()
    s_li.remove(22)
    s_li.print_list()
    print(s_li.find('&'))
    print(s_li.get(10))
    print(s_li.length())

"""results
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
999 
1 2 3 4 5 6 7 8 9 10 
11 12 13 14 15 16 17 18 19 20 
1 2 3 4 5 6 7 8 9 77 
11 12 13 14 15 16 17 18 19 20 
77
10
21
==============================
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * & 
* * * * $ * * * * * 
* * 
* * * * * * * * * & 
* * * * $ * * * * * 
* @ 
* * * * * * * * * & 
* * * * $ * * * * * 
* 
10
&
22

Process finished with exit code 0
"""


```

## 3 Performance

### 3.1 LinearList vs LinkedList

The essential distinction between linearlist and linkedlist is that linearlists store elements in contiguous memory locations which make its nodes can be easily access with a specific index, while linkedlists store things in random locations(in normal conditions) and use additional tags in its nodes to make every node linked.


### 3.2 Performance Test

Here I use the `insert` operation to test my previous implementation of linearlist and linkedlist.

#### 3.2.1 LINEARLIST_H_
```c++
// linearlist.h

#ifndef LINEARLIST_H_
#define LINEARLIST_H_


#include <cstring>
#include <iostream>

namespace linear {

static int LIST_INIT_SIZE = 100000;
static int LIST_EXPAND_SIZE = 100000;

// typedef int Item;
template<class Item>
class List {
   private:
    Item* p_items_;
    int capacity_;
    int length_;
    bool expand() {
        Item* temp;
        try {
            temp = new Item[capacity_ + LIST_EXPAND_SIZE];
            memcpy(temp, p_items_, length_ * sizeof(Item));
        } catch (std::bad_alloc e) {
            std::cout << "Error: allocate new memory failed.\n";
            std::cout << e.what();
            return false;
        }
        delete[] p_items_;
        p_items_ = temp;
        capacity_ += LIST_EXPAND_SIZE;
        // std::cout << "expanded from " << capacity_-LIST_EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    };

   public:
    List();
    ~List();  // new for `delete`
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);  // little change
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    bool isfull() const;
};


template<class Item>
List<Item>::List() {
    p_items_ = new Item[LIST_INIT_SIZE];
    capacity_ = LIST_INIT_SIZE;
    length_ = 0;
}

template<class Item>
List<Item>::~List() {
    delete[] p_items_;
}

template<class Item>
bool List<Item>::insert(int i, Item e) {  // updated
    if (isfull()) {
        if (!expand())
            return false;
    }
    for (int index = length_; index >= i; --index) {
        p_items_[index] = p_items_[index - 1];
    }
    p_items_[i - 1] = e;
    ++length_;
    return true;
}

template<class Item>
int List<Item>::length() {
    return length_;
}

template<class Item>
bool List<Item>::isempty() const {
    if (length_ == 0) {
        return true;
    } else {
        return false;
    }
}

template<class Item>
bool List<Item>::isfull() const {
    if (length_ == capacity_) {
        return true;
    } else {
        return false;
    }
}

}  // namespace

#endif
```


#### 3.2.2 LINKEDLIST_H_ 

```c++
// linkedlist.h
#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_

#include <cstring>
#include <iostream>

namespace linked {

template <class Item>
class Node {
   public:
    Item item;
    Node* next;
};

template <class Item>
class List {
   private:
    Node<Item>* head;
    int length_;

   public:
    List();
    ~List();
    bool insert(int i, Item e);
    bool remove(int i);
    bool replace(int i, Item e);
    bool get(int i, Item& e);
    int find(Item e);
    void printlist() const;
    // void destroylist();
    int length();
    bool isempty() const;
    // bool isfull() const;
};

template <class Item>
List<Item>::List() {
    head = new Node<Item>;
    head->next = NULL;
    // std::cout<<"head location: " << head << "\n";
    length_ = 0;
}

template <class Item>
List<Item>::~List() {
    // for item in length, delete node->next
    Node<Item>* p = head->next;
    while (p != NULL) {
        Node<Item>* q = p;
        p = p->next;
        delete q;
    }
    delete head;
}

template <class Item>
bool List<Item>::insert(int i, Item e) {
    if (i < 1 || i > length_ + 1)
        return false;

    Node<Item>* p = head;
    while (--i) {
        p = p->next;
    }

    Node<Item> * node = new Node<Item>();
    node->item = e;
    node->next = p->next;
    p->next = node;

    ++length_;
    return true;
}

}  // namespace

#endif
```

#### 3.2.3 Test Code and Result

```c++
// performance_test.cpp
#include <ctime>
#include <iostream>
#include "linearlist.h"
#include "linkedlist.h"

void test_linearlist_insert_time_best_situation(int amount) {
    using namespace linear;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(i+1, i);
    }
    // mylist.printlist();
    end = clock();
    std::cout<<"linearlist insert "<< amount << " items best  situation cost time: " << end - start << std::endl;
}

void test_linearlist_insert_time_worst_situation(int amount) {
    using namespace linear;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(1, i);
    }
    // mylist.printlist();
    end = clock();
    std::cout<<"linearlist insert "<< amount << " items worst situation cost time: " << end - start << std::endl;
}

void test_linkedlist_insert_time_best_situation(int amount){
    using namespace linked;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(1, i);
    }
    end = clock();
    std::cout<<"linkedlist insert "<< amount << " items best  situation cost time: " << end - start << std::endl;
}

void test_linkedlist_insert_time_worst_situation(int amount){
    using namespace linked;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(i+1, i);
    }
    end = clock();
    std::cout<<"linkedlist insert "<< amount << " items worst situation cost time: " << end - start << std::endl;
}



int main(int argc, char const* argv[]) {

    test_linearlist_insert_time_best_situation(100000);
    test_linkedlist_insert_time_best_situation(100000);
    test_linearlist_insert_time_worst_situation(100000);
    test_linkedlist_insert_time_worst_situation(100000);
   
    test_linearlist_insert_time_best_situation(1000000);
    test_linkedlist_insert_time_best_situation(1000000);
    test_linearlist_insert_time_worst_situation(1000000);
    test_linkedlist_insert_time_worst_situation(1000000);


    return 0;
}

/*
linearlist insert 100000 items best  situation cost time: 1
linkedlist insert 100000 items best  situation cost time: 223
linearlist insert 100000 items worst situation cost time: 9013
linkedlist insert 100000 items worst situation cost time: 20656
linearlist insert 1000000 items best  situation cost time: 10
linkedlist insert 1000000 items best  situation cost time: 2456
linearlist insert 1000000 items worst situation cost time: 902397
linkedlist insert 1000000 items worst situation cost time: 2873597
*/

```

#### 3.2.4 Result Analysis

For the `insert` operation, the linkedlist should theoretically be more efficient then the linearlist, because the linkedlist only need to change the links within three nodes, while the linearlist need to move all nodes after the inserted node.Considering that in the linkedlist, the `lookup` operation takes as much time as moving nodes in the linearlist, insertion time should be basically the same. 

However, the test result is not very consistent with the theory. Review the most relevant codes:

```c++
// LinearList
static int LIST_INIT_SIZE = 100000;
static int LIST_EXPAND_SIZE = 100000;

LinearList::expand() {
        Item* temp;
        try {
            temp = new Item[capacity_ + LIST_EXPAND_SIZE];
            memcpy(temp, p_items_, length_ * sizeof(Item));
        } catch (std::bad_alloc e) {
            return false;
        }
        delete[] p_items_;
        p_items_ = temp;
        capacity_ += LIST_EXPAND_SIZE;
        return true;
};

LinearList::insert(int i, Item e) {
    if (isfull()) {
        if (!expand())
            return false;
    }
    for (int index = length_; index >= i; --index) {
        p_items_[index] = p_items_[index - 1];
    }
    p_items_[i - 1] = e;
    ++length_;
    return true;
}
```

```c++
// LinkedList
LinkedList::insert(int i, Item e) {
    if (i < 1 || i > length_ + 1)
        return false;

    Node<Item>* p = head;
    while (--i) {
        p = p->next;
    }

    Node<Item> * node = new Node<Item>();
    node->item = e;
    node->next = p->next;
    p->next = node;

    ++length_;
    return true;
}
```

Seems there are much more atomic operations in the linkedlist code then in the linearlist, well, the proformance depends on the implementation.
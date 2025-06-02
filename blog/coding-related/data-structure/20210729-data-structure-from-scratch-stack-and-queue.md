# Data Structure from Scratch: Stack & Queue

*Posted on 2021.07.29 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

- [Data Structure from Scratch: Stack & Queue](#data-structure-from-scratch-stack--queue)
  - [1. Stack Array Implementation](#1-stack-array-implementation)
  - [2. Stack Linkedlist Implementation](#2-stack-linkedlist-implementation)
  - [3. Stack in Use](#3-stack-in-use)
    - [3.1. Number System Conversion](#31-number-system-conversion)
    - [3.2. Bracket Matching Check](#32-bracket-matching-check)
  - [4. Queue Array Implementation](#4-queue-array-implementation)
  - [5. Queue Linkedlist Implementation](#5-queue-linkedlist-implementation)
  - [6. Queue in Use: Simulata Stack with Queue](#6-queue-in-use-simulata-stack-with-queue)


## 1. Stack Array Implementation

Header:

```c++
// stack.h
#ifndef STACK_H_
#define STACK_H_

#include<cstring>
#include<iostream>

static const int INIT_SIZE = 100;
static const int EXPAND_SIZE = 100;

template<class Item>
class Stack
{
private:
    Item* p_stack_;
    int top_;
    int capacity_;
    int length_;
    bool expand(){
        Item* temp;
        try{
            temp = new Item[capacity_ + EXPAND_SIZE];
            memcpy(temp, p_stack_, length_ * sizeof(Item));
        }catch(std::bad_alloc e){
            std::cerr << e.what() << '\n';
            return false;
        }
        delete [] p_stack_;
        p_stack_ = temp;
        capacity_ += EXPAND_SIZE;
        std::cout << "expanded from " << capacity_ - EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    }
    
public:
    Stack();
    ~Stack();
    Item pop();
    bool push(Item item);
    bool suicide();
    bool clear();
    bool isempty();
    bool isfull();
    int length();
};

template<class Item>
Stack<Item>::Stack(){
    p_stack_ = new Item[INIT_SIZE];
    top_ = -1;
    capacity_ = INIT_SIZE;
    length_ = 0;
}

template<class Item>
Stack<Item>::~Stack(){
    delete [] p_stack_;
}

template<class Item>
bool Stack<Item>::push(Item item){
    if(isfull()){
        if(!expand()){
            return false;
        }
    }
    p_stack_[top_+1] = item;
    ++top_;
    ++length_;
    return true;
}

template<class Item>
Item Stack<Item>::pop(){
    if(isempty()){
        std::cout<<"!pop failed: an empty stack"<<std::endl;
        return NULL;  // ...
    }
    Item e = p_stack_[top_];
    --top_;
    --length_;
    return e;
}

template<class Item>
bool Stack<Item>::suicide(){
    delete [] p_stack_;
    return true;
}

template<class Item>
bool Stack<Item>::clear(){
    top_ = -1;
    length_ = 0;
    return true;
}

template<class Item>
bool Stack<Item>::isfull(){
    if(length_ == capacity_)
        return true;
    else
        return false;
}

template<class Item>
bool Stack<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
int Stack<Item>::length(){
    return length_;
}

#endif

```

Test:

```c++
// stack_test.cpp
#include "stack.h"
#include <iostream>

using std::cout;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    cout<<stack.length()<<std::endl;
    for (int i = 0; i < 100; i++)
    {
        stack.push(i);
    }
    cout<<stack.length()<<std::endl;
    cout<<stack.isempty()<<std::endl;
    cout<<stack.isfull()<<std::endl;
    stack.push(101);
    cout<<stack.pop()<<std::endl;
    
    return 0;
}

/*
0
100
0
1
expanded from 100 to 200
101
*/
```

## 2. Stack Linkedlist Implementation

Header:

```c++
// stack.h
#ifndef STACK_H_
#define STACK_H_

#include <iostream>
using std::cout;
using std::endl;


template<class Item>
class Node{
public:
    Item data;
    Node* next;
};


template<class Item>
class Stack{
private:
    Node<Item>* p_base_;
    Node<Item>* p_top_;
    int length_;
    
public:
    Stack();
    ~Stack();
    Item pop();
    bool push(Item item);
    bool suicide();
    bool clear();
    bool isempty();
    // bool isfull();
    int length();
};

template<class Item>
Stack<Item>::Stack(){
    
    p_base_ = new Node<Item>;
    cout<<"p_base_ = "<<p_base_<<endl;
    cout<<"p_top_ = "<<p_top_<<endl;
    p_base_->next = p_base_;
    p_top_ = p_base_;
    cout<<"p_top_->next = "<<p_top_->next<<endl;
    length_ = 0;
}

template<class Item>
Stack<Item>::~Stack(){
    while (length_ != 0)
    {
        pop();
    }
    delete p_base_;
}

template<class Item>
bool Stack<Item>::suicide(){
    while (length_ != 0)
    {
        pop();
    }
    delete p_base_;
    return true;
}

template<class Item>
bool Stack<Item>::clear(){
    while (length_ != 0)
    {
        pop();
    }
    return true;
}

template<class Item>
bool Stack<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
bool Stack<Item>::push(Item e){
    cout<<"before push, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    Node<Item>* new_node = new Node<Item>;
    new_node->data = e;
    new_node->next = p_top_;
    p_top_ = new_node;
    ++length_;
    cout<<"after  push, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    return true;
}

template<class Item>
Item Stack<Item>::pop(){
    cout<<"before pop, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    if(length_ == 0){
        std::cout<<"!pop failed: an empty stack"<<std::endl;
        return 0;
    }
    Item e = p_top_->data;
    Node<Item>* temp = p_top_;
    p_top_ = p_top_->next;
    delete temp;
    --length_;
    cout<<"after  pop, p_top_ = "<<p_top_<<"  p_top_->next = "<<p_top_->next<<endl;
    return e;
}

template<class Item>
int Stack<Item>::length(){
    return length_;
}

#endif
```

Test:

```c++
// stack_test.cpp
#include "stack.h"
#include <iostream>

using std::cout;
using std::endl;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    cout<<"stack length is: "<<stack.length()<<endl;
    for (int i = 0; i < 10; i++)
    {
        stack.push(i);
    }
    cout<<"stack length is: "<<stack.length()<<endl;
    stack.push(101);
    cout<<"stack length is: "<<stack.length()<<endl;
    cout<<stack.pop()<<endl;
    while (stack.length()!=0)
    {
        cout<<stack.pop()<<endl;
    }
    // stack.suicide();
    cout<<"stack length is: "<<stack.length()<<endl;
    
    return 0;
}

/*
p_base_ = 0x6d1e10
p_top_ = 0x401519
p_top_->next = 0x6d1e10
stack length is: 0
before push, p_top_ = 0x6d1e10  p_top_->next = 0x6d1e10
after  push, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
before push, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
after  push, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
before push, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
after  push, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
before push, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
after  push, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
before push, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
after  push, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
before push, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
after  push, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
before push, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
after  push, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
before push, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
after  push, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
before push, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
after  push, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
before push, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
after  push, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
stack length is: 10
before push, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
after  push, p_top_ = 0x6d41b0  p_top_->next = 0x6d4170
stack length is: 11
before pop, p_top_ = 0x6d41b0  p_top_->next = 0x6d4170
after  pop, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
101
before pop, p_top_ = 0x6d4170  p_top_->next = 0x6d4130
after  pop, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
9
before pop, p_top_ = 0x6d4130  p_top_->next = 0x6d40f0
after  pop, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
8
before pop, p_top_ = 0x6d40f0  p_top_->next = 0x6d40b0
after  pop, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
7
before pop, p_top_ = 0x6d40b0  p_top_->next = 0x6d4070
after  pop, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
6
before pop, p_top_ = 0x6d4070  p_top_->next = 0x6d4030
after  pop, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
5
before pop, p_top_ = 0x6d4030  p_top_->next = 0x6d3ff0
after  pop, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
4
before pop, p_top_ = 0x6d3ff0  p_top_->next = 0x6d3fb0
after  pop, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
3
before pop, p_top_ = 0x6d3fb0  p_top_->next = 0x6d1a20
after  pop, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
2
before pop, p_top_ = 0x6d1a20  p_top_->next = 0x6d19e0
after  pop, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
1
before pop, p_top_ = 0x6d19e0  p_top_->next = 0x6d1e10
after  pop, p_top_ = 0x6d1e10  p_top_->next = 0x6d1e10
0
stack length is: 0
*/
```

## 3. Stack in Use

### 3.1. Number System Conversion

Code:

```c++
// 1_number_system_conversion.cpp

/**
 * convert decimal to binary
 * decimal N = (N div d)*d + N mod d
 */

#include "stack.h"
#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int main(int argc, char const *argv[])
{
    Stack<int> stack;
    int decimal;
    while (1)
    {
        cout << "input a decimal: ";
        cin >> decimal;
        while (decimal)
        {
            stack.push(decimal % 2);
            decimal /= 2;
        }
        int i=0;
        cout<< "the binary is: ";
        while (!stack.isempty())
        {
            cout<<stack.pop();
            ++i;
            if(i%4 == 0 && i != 0)
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}

/*
input a decimal: 16
the binary is: 1000 0
input a decimal: 1024
the binary is: 1000 0000 000
input a decimal: 3245234
the binary is: 1100 0110 0001 0010 1100 10
*/
```

### 3.2. Bracket Matching Check

Code:

```c++
// 2_bracket_matching_check.cpp

/**
 * ( = 40
 * ) = 41
 * [ = 91
 * ] = 93
 * { = 123
 * } = 125
 */

#include "stack.h"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    Stack<char> stack;
    char formula[100];
    while (1)
    {   
        cout << "input a formula: ";
        cin.getline(formula, 101);
        bool flag = true;
        stack.clear();
        for (int i = 0; i < strlen(formula); i++)
        {
            char temp = formula[i];
            if(temp == 40 || temp == 91 || temp == 123){
                stack.push(temp);
            }
            if(temp == 41 || temp == 93 || temp == 125){
                char left_bracket = stack.pop();
                if(left_bracket == temp-1 || left_bracket == temp-2){
                    //
                }else{
                    flag = false;
                    break;
                }
            }
        }
        if(flag==true && stack.length()==0){
            cout<<"check passed"<<endl;
        }else{
            cout<<"bad matching"<<endl;
        }
    }
    
    return 0;
}

/*
input a formula: {
bad matching     
input a formula: []
check passed     
input a formula: {}{}{}{
bad matching     
input a formula: }
!pop failed: an empty stack
bad matching
input a formula: {sdfsdf[sdf]sdfs[sd[sdf]sdf]sdf(sdf[sdf[[[]]]])}
check passed
input a formula:
check passed
input a formula: ...(-.-)... 
check passed
*/
```


## 4. Queue Array Implementation

Header:

```c++
// queue.h
#ifndef QUEUE_H_
#define QUEUE_H_

#include <iostream>
using std::cout;

static const int INIT_SIZE = 10;
static const int EXPAND_SIZE = 10;

template<class Item>
class Queue
{
private:
    Item* p_queue_;
    int capacity_;
    int length_;
    int head_;
    int tail_;
    bool expand(){
        Item* temp = new Item[capacity_ + EXPAND_SIZE];
        for (int i = 0; i < capacity_; i++)
        {
            temp[i] = p_queue_[i];
        }
        delete [] p_queue_;
        p_queue_ = temp;
        capacity_ += EXPAND_SIZE;
        std::cout << "expanded from " << capacity_ - EXPAND_SIZE << " to " << capacity_ << "\n";
        return true;
    }
public:
    Queue(/* args */);
    ~Queue();
    bool enqueue(Item e);
    Item dequeue();
    bool isempty();
    bool clear();
    int length();
};

template<class Item>
Queue<Item>::Queue(/* args */)
{
    p_queue_ = new Item[INIT_SIZE];
    capacity_ = INIT_SIZE;
    length_ = 0;
    head_ = 0;
    tail_ = 0;
}

template<class Item>
Queue<Item>::~Queue()
{
    delete [] p_queue_;
}

template<class Item>
bool Queue<Item>::enqueue(Item e)
{
    if(tail_ == capacity_){
        if(head_ != 0){
            //move items to the head of the queue, then consider expanding
            for (int i = 0; i < length_; i++)
            {
                p_queue_[i] = p_queue_[head_ + i];
            }
            head_ = 0;
            tail_ = length_;
        }else{  // length_ == capacity_
            if (!expand()){
                return false;
            }
        }
    }
    p_queue_[tail_] = e;
    length_++;
    tail_++;
    return true;
}

template<class Item>
Item Queue<Item>::dequeue()
{
    if (isempty())
    {
        cout << "!dequeue failed: an empty queue\n";
        return NULL;
    }
    Item e = p_queue_[head_];
    head_++;
    length_--;
    return e;   
}

template<class Item>
bool Queue<Item>::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
bool Queue<Item>::clear(){
    head_ = 0;
    tail_ = 0;
    length_ = 0;
}

template<class Item>
int Queue<Item>::length(){
    return length_;
}

#endif
```

Test:

```c++
// queue_test.cpp
#include "queue.h"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    Queue<int> queue;
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 10; i++)
    {
        queue.enqueue(i);
    }
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 10; i++)
    {
        cout << queue.dequeue() << endl;
    }
    
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 50; i++)
    {
        queue.enqueue(i);
    }
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 57; i++)
    {
        cout << queue.dequeue() << endl;
    }
    cout << "queue length = " << queue.length() << endl;
    

    return 0;
}

/*
queue length = 0
queue length = 10
0
1
2
3
4
5
6
7
8
9
queue length = 0
expanded from 10 to 20
expanded from 20 to 30
expanded from 30 to 40
expanded from 40 to 50
queue length = 50
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
!dequeue failed: an empty queue
0
queue length = 0
*/

```

## 5. Queue Linkedlist Implementation

Header:

```c++
// queue.h
#ifndef QUEUE_H_
#define QUEUE_H_

#include <iostream>
using std::cout;

template<class Item>
class Node{
public:
    Item data;
    Node* next;
};

template<class Item>
class Queue
{
private:
    Node<Item>* head;
    Node<Item>* tail;
    int length_;

public:
    Queue(/* args */);
    ~Queue();
    bool enqueue(Item e);
    Item dequeue();
    bool isempty();
    bool clear();
    int length();
};

template<class Item>
Queue<Item>::Queue(/* args */)
{
    head = new Node<Item>;
    head->next = head;
    tail = head;
    length_ = 0;
}

template<class Item>
Queue<Item>::~Queue()
{
    clear();
}

template<class Item>
bool Queue<Item>::enqueue(Item e){
    tail->data = e;
    Node<Item>* temp = new Node<Item>;
    tail->next = temp;
    tail = temp;
    length_++;
    return true;
}

template<class Item>
Item Queue<Item>::dequeue(){
    if(isempty()){
        cout<< "!dequeue failed, an empty queue";
        return NULL;
    }
    Item e = head->data;
    Node<Item>* temp = head;
    head = head->next;
    delete temp;
    length_--;
    return e;
}

template<class Item>
bool Queue<Item>::clear(){
    Node<Item>* temp;
    while (length_ != 0)
    {
        temp = head;
        head = head->next;
        delete temp;
        length_--;
    }
    cout<<"head = " << head << "\n";
    cout<<"tail = " << tail << "\n";
    return true;
}

template<class Item>
bool Queue<Item>::isempty(){
    if (length_ == 0)
        return true;
    else
        return false;
}

template<class Item>
int Queue<Item>::length(){
    return length_;
}

#endif
```

Test:

```c++
// queue_test.cpp
#include "queue.h"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    Queue<int> queue;
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 10; i++)
    {
        queue.enqueue(i);
    }
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 10; i++)
    {
        cout << queue.dequeue() << endl;
    }
    
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 50; i++)
    {
        queue.enqueue(i);
    }
    cout << "queue length = " << queue.length() << endl;
    for (int i = 0; i < 57; i++)
    {
        cout << queue.dequeue() << endl;
    }
    cout << "queue length = " << queue.length() << endl;
    

    return 0;
}

/*
queue length = 0 
queue length = 10
0
1
2
3
4
5
6
7
8
9
queue length = 0 
queue length = 50
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
!dequeue failed, an empty queue0
queue length = 0
head = 0x632930
tail = 0x632930
*/
```

## 6. Queue in Use: Simulata Stack with Queue

Header:

```c++
// simulate_stack_using_two_queues.h
#include "queue.h"
#include <iostream>

using namespace std;

class SimulateStack
{
private:
    Queue<int>* q1;
    Queue<int>* q2;
    int length_;

public:
    SimulateStack();
    ~SimulateStack();
    int pop();
    bool push(int i);
};

SimulateStack::SimulateStack()
{
    q1 = new Queue<int>;
    q2 = new Queue<int>;
    length_ = 0;
}

SimulateStack::~SimulateStack()
{
    delete q1;
    delete q2;
}

bool SimulateStack::push(int i){
    q1->enqueue(i);
    length_ ++;
    return true;
}

int SimulateStack::pop(){
    if(length_ > 0){
        while (q1->length() > 1)
        {
            q2->enqueue(q1->dequeue());
        }
        int result = q1->dequeue();
        length_ --;

        while (q2->length() > 0)
        {
            q1->enqueue(q2->dequeue());
        }
        return result;
    }else{
        cout<<"empty! pop failed."<<endl;
        return NULL;
    }
}
```


Test:

```c++
// test.cpp
#include "simulate_stack_using_two_queues.h"
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    SimulateStack* stack = new SimulateStack();
    stack->push(1);
    stack->push(2);
    stack->push(3);
    cout<< stack->pop()<<endl;
    stack->push(4);
    stack->push(5);
    stack->push(6);
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    cout<< stack->pop()<<endl;
    return 0;
}

/*
3
6
5
4
2
1
empty! pop failed.
0
*/
```
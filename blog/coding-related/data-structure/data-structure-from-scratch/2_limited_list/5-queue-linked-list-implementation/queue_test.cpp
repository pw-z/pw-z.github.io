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
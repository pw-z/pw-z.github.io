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

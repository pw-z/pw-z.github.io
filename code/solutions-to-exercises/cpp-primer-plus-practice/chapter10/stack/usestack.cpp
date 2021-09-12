#include <iostream>
#include "stack.h"

int main(int argc, char const *argv[])
{
    using namespace std;
    Stack st;
    char order;
    string stuff;
    cout << "A to add stuff, P to pop stuff, Q to quit.\n";
    while (cin >> order && order != 'q' && order != 'Q')
    {
        switch(order){
            case 'A':
            case 'a': {
                cout << "enter a stuff name to add: ";
                cin >> stuff;
                if (st.isfull())
                {
                    cout << "stack already full\n";
                }
                else{
                    st.push(stuff);
                    cout << stuff << " was pushed into stack.\n";
                }
                break;
            }
            case 'P':
            case 'p':{
                if (st.isempty())
                {
                    cout << "stack already empty\n";
                }
                else{
                    stuff = st.pop();
                    cout << "pop a stuff named " << stuff << ".\n";
                }
                break;
            }    
        }
        cout << "A to add stuff, P to pop stuff, Q to quit.\n";
    }
    cout << "BEY\n";
    return 0;
}

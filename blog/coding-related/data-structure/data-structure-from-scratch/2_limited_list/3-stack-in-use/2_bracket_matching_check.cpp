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
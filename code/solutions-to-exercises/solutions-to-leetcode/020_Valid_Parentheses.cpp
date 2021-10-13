#include<string>
using std::string;
class Solution {
public:
    /*
    ( = 40
    ) = 41
    { = 123
    } = 125
    [ = 91
    ] = 93
    */
    bool isValid(string s) {
        int stack[5000];
        int cur=0;
        for(char c: s){
            if(c == '(' || c=='{' || c=='['){
                stack[cur++] = c;
            }else{
                if(cur == 0) return false;
                else{
                    if(c == ')'){
                        if(stack[--cur]+1 != c) return false;
                    }else{
                        if(stack[--cur]+2 != c) return false;
                    }
                }
            }
        }
        return cur==0? true: false;
    }
};
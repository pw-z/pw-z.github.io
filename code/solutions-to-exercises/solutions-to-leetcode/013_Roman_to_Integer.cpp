#include<iostream>
#include<unordered_map>

using namespace std;

class Solution {
    unordered_map<char, int> switch_map;
public:
    Solution(){
        switch_map['I'] = 1;
        switch_map['V'] = 5;
        switch_map['X'] = 10;
        switch_map['L'] = 50;
        switch_map['C'] = 100;
        switch_map['D'] = 500;
        switch_map['M'] = 1000;
    }
    int romanToInt(string s) {
        cout<<"s = "<<s<<endl;

        int result=0;
        int len = s.length();
        cout<<"len = "<<len<<endl;
        for(int i=0; i<len; ++i){
            if(s[i] == 'I' && s[i+1]== 'V'){
                result += 4;
                ++i;
            }else if (s[i] == 'I' && s[i+1]== 'X'){
                result += 9;
                ++i;
            }else if (s[i] == 'X' && s[i+1]== 'L'){
                result += 40;
                ++i;
            }else if (s[i] == 'X' && s[i+1]== 'C'){
                result += 90;
                ++i;
            }else if (s[i] == 'C' && s[i+1]== 'D'){
                result += 400;
                ++i;
            }else if (s[i] == 'C' && s[i+1]== 'M'){
                result += 900;
                ++i;
            }else{
                result+= switch_map[s[i]];
            }
        }
        return result;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol = Solution();
    sol.romanToInt("MCMXCIV");
    return 0;
}

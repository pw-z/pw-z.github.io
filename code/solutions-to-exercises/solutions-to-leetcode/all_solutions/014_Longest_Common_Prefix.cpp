#include<string>
using std::string;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int len_last, len_cur;
        string prefix = strs[0];
        for(string &s: strs){
            len_cur = 0;
            for(int i=0; i<s.size(); ++i){
                if(s[i] == prefix[i]) ++len_cur;
                else break;
            }
            if(len_cur == 0) return "";
            else prefix = prefix.substr(0, len_cur);
        }
        return prefix;
    }
};

/*
执行用时：4 ms, 在所有 C++ 提交中击败了82.66% 的用户
内存消耗：8.8 MB, 在所有 C++ 提交中击败了87.49% 的用户
*/
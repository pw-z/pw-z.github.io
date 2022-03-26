#include <algorithm>
//#include <vector>
#include <iostream> // for swap() func
#include <string>

using std::swap;
using std::string;
//using std::cin;
//using std::cout;

class Solution {
public:
    /* 双指针定位字串、逆转子串， 两个指针遍历完整个串结束*/
    string reverseWords(string s) {
        int len = s.length();
        int low = 0;
        while (low < len){
            // low 作为每次子串的起点，high从low开始向右找到最近的空格
            int high = low;
            while (high < len && s[high] != ' '){
                ++high;
            }

            // 执行swap逻辑，执行前记录下high的位置，下一次处理从该位置开始
            int tag = high;
            --high;
            while (low < high){
                swap(s[low], s[high]);
                ++low;
                --high;
            }

            // 更新low到下一个子串开头（可能超出len，则逻辑结束）
            low = tag+1;
        }
        return s;
    }
};
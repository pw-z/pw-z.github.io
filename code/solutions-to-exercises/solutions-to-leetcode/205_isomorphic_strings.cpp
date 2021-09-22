/*
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

#include<string>
#include<unordered_map>
#include<iostream>
using std::cout;
using std::string;
using std::unordered_map;


// class Solution {
// public:
//     void get_pattern(string s, int pattern[]){
//         for (int i = 0; i < s.size(); i++)
//         {
//             pattern[i] = i;
//         }
        
//     }
//     bool isIsomorphic(string s, string t) {
//         int* s_pattern = new int[s.size()]();
//         get_pattern(s, s_pattern);
//         for (int i = 0; i < s.size(); i++)
//         {
//             cout<<s_pattern[i]<<"\n";
//         }
//         return true;
//     }
// };


class Solution {
public:
    bool isIsomorphic(string s, string t) {
        // unordered_map<char, char> hashmap;
        unordered_map<char, char> hashmap_s;
        unordered_map<char, char> hashmap_t;
        for (int i = 0; i < s.size(); ++i)
        {
            char char_s = s.at(i);
            char char_t = t.at(i);

            if (hashmap_s.count(char_s) > 0 && hashmap_s[char_s] != char_t){
                return false;
            }else if (hashmap_t.count(char_t) > 0 && hashmap_t[char_t] != char_s){
                return false;
            }else{
                hashmap_s[char_s] = char_t;
                hashmap_t[char_t] = char_s;
            }
            
            // if(hashmap.count(char_s) > 0){
            //     if(hashmap[char_s] != char_t && hashmap_t.count()){
            //         return false;
            //     }
            // }else{
            //     hashmap_s[char_s] = char_t;
            //     hashmap_t[char_t] = char_s;
            // }
        }
        return true;
    }
};


int main(int argc, char const *argv[])
{
    Solution* obj = new Solution();
    string s = "badc";
    string t = "faec";
    bool result = obj->isIsomorphic(s, t);
    cout<<result<<"\n";

    return 0;
}

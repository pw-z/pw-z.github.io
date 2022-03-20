#include<string>
#include<unordered_map>
using std::unordered_map;
using std::string;

class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> hashmap;
        // for(int i = 0; i < s.size(); ++i){
        //     char cur = s.at(i);
        //     if(hashmap.count(cur) > 0){
        //         hashmap[cur]++;
        //     }else{
        //         hashmap[cur] = 1;
        //     }
        // }
        for(char c: s){
            ++hashmap[c];
        }
        for(int i = 0; i < s.size(); ++i){
            char cur = s.at(i);
            if(hashmap[cur] == 1){
                return i;
            }
        }
        return -1;
    }
};
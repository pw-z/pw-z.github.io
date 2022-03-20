#include<vector>
#include<string>
#include<unordered_map>
// #include<unordered_set>
using std::vector;
using std::string;
using std::unordered_map;
// using std::unordered_set;

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        vector<string> result;
        int min_sum = -1;
        unordered_map<string, int> hashmap;

        for(int i = 0; i < list1.size(); ++i){
            hashmap[list1[i]] = i;
        }
        for(int i = 0; i < list2.size(); ++i){
            string s2 = list2[i];
            if(hashmap.count(s2) > 0){
                int sum = hashmap[s2] + i;
                if(min_sum == -1){
                    min_sum = sum;
                    result.push_back(s2);
                }else if(sum < min_sum){
                    min_sum = sum;
                    result.clear();
                    result.push_back(s2);
                }else if(sum == min_sum){
                    result.push_back(s2);
                }
            }
        }
        return result;
    }
};
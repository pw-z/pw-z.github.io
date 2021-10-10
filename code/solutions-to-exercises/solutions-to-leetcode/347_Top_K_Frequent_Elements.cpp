#include<unordered_map>
#include<vector>
using std::vector;
using std::unordered_map;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for(int &num: nums){
            ++count[num];
        }

        
    }
};
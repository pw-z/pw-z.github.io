#include<vector>
#include<unordered_set>

using std::vector;
using std::unordered_set;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> hashset;
        vector<int> result;
        for(int num: nums1){
            hashset.insert(num);
        }
        for(int num: nums2){
            if(hashset.count(num) > 0){
                hashset.erase(num);
                result.push_back(num);
            }
        }
        return result;
    }
};
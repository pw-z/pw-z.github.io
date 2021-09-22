#include<unordered_map>
using std::unordered_map;

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_map<int, int> intersection_count;
        for(int num: nums1){
            ++intersection_count[num];
        }
        for(int num: nums2){
            if(intersection_count[num] >0){
                result.push_back(num);
                --intersection_count[num];
            }
        }
        return result;
    }
};
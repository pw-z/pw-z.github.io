#include <vector>
using std::vector;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int l=0,r=0;
        for(;r<nums.size();++r){
            if(nums[r] != val){
                nums[l] = nums[r];
                ++l;
            }
        }
        return l;
    }
};
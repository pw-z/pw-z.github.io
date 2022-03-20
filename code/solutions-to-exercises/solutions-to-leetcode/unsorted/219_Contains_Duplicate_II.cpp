class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> hashmap;  // <num, last_loc>
        for(int i=0; i<nums.size(); ++i){
            int num = nums[i];
            if(hashmap.count(num) > 0 && i-hashmap[num] <= k){
                return true;
            }
            hashmap[nums[i]] = i;
        }
        return false;
    }
};
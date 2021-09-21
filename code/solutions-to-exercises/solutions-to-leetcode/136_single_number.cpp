class Solution {
public:
    /*
    // 空间复杂度为O(N)
    int singleNumber(vector<int>& nums) {
        unordered_set<int> hashset;
        for(int num: nums){
            if(hashset.count(num) == 0){
                hashset.insert(num);
            }else{
                hashset.erase(num);
            }
        }
        return *hashset.begin();
    }
    */

   // 借助异或运算实现空间复杂度O(1)
    int singleNumber(vector<int>& nums) {
        int result = 0;
        for(int num: nums){
            result ^= num;
        }
        return result;
    }
};

#include<vector>
#include<unordered_map>
using namespace std;

class RandomizedSet {
    vector<int> nums;
    unordered_map<int, int> num2idx;
    int index = -1;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if(num2idx.count(val) > 0) return false;
        else{
            // nums[++index] = val;
            ++index;
            num2idx[val] = index;
            nums.push_back(val);
            return true;
        }
    }
    
    bool remove(int val) {
        if(num2idx.count(val)){
            int pos = num2idx[val];
            nums[pos] = nums[index];
            num2idx[nums[pos]] = pos;
            nums.pop_back();
            num2idx.erase(val);
            --index;
            return true;
        }else{
            return false;
        }
    }
    
    int getRandom() {
        /*
        rand()返回一个从0到最大随机数的任意整数，
        最大随机数的大小通常是固定的一个大整数。
        */
         return nums[rand() % (index + 1)];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */


/*
index是非必须的，参考如下代码，更精简：

作者：zan-wu-ni-cheng
链接：https://leetcode-cn.com/problems/insert-delete-getrandom-o1/solution/c-hashshu-zu-by-zan-wu-ni-cheng-9oas/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
class RandomizedSet {
public:
    unordered_map<int,int> hash;
    vector<int> arr;
    /** Initialize your data structure here. */
    RandomizedSet() {

    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(hash.count(val))return 0;
        hash[val]=arr.size();
        arr.push_back(val);
        return 1;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(!hash.count(val))return 0;
        hash[arr.back()]=hash[val];
        arr[hash[val]]=arr.back();
        hash.erase(val);
        arr.pop_back();
        return 1;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return arr[rand()%arr.size()];
    }
};

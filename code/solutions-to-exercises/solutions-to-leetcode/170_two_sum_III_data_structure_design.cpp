class TwoSum {
    unordered_map<long long, int> nums;
public:
    TwoSum() {
        
    }
    
    void add(int number) {
        ++nums[number];
    }
    
    bool find(int value) {
        for(auto it=nums.begin(); it != nums.end(); ++it){
            int target = value - it->first;
            if(nums.count(target)){
               if(target != it->first || (target == it->first && nums[target]>1)){
                    return true;
                }
                /*
                nums.count(target)命中后：
                如下这样判断不可以，会导致没有遍历完所有可能答案，提前按照无答案返回false
                if(target == it->first && nums[target]<=1){
                    return false;
                }
                return true;
                */
            }
        }
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum* obj = new TwoSum();
 * obj->add(number);
 * bool param_2 = obj->find(value);
 */
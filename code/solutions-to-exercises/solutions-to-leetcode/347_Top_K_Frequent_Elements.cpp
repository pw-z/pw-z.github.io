#include<unordered_map>
#include<vector>
using std::vector;
using std::unordered_map;

class Solution {
public:
    /*
    O(nlogk)整体思路：
        1. 数数，将结果存入hashmap，key=number，value=counts
        2. 使用map的前K个元素的counts建立大小为K的小根堆
        3. 使用map的后续元素不断更新小根堆
    需要进行的工作：
        1. 主流程，数数，建堆，更新堆
        2. 实现小根堆的更新算法，即将小于堆顶的元素替换成堆顶，然后下沉到正确位置
    */
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        for(int &num: nums){
            ++count[num];
        }

        
    }
};
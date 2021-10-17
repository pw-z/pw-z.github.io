#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;


class Solution {
public:
    void heapify(vector<vector<int>> &heap, int k){
        int len = heap.size();
        int cur = k, l, r, min;
        vector<int> temp;
        while (cur < len/2)
        {
            l = cur*2+1;
            r = l+1;
            min = cur;
            if(l < len && heap[l][1] < heap[cur][1]) min=l;
            if(r < len && heap[r][1] < heap[min][1]) min=r;
            if(min == cur) return;
            
            temp = heap[cur];
            heap[cur] = heap[min];
            heap[min] = temp;

            if(min == l) cur=l;
            else cur=r;
        }
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // freq --> frequency, heap --> min_heap
        vector<vector<int>> freq_list;
        vector<vector<int>> heap;
        unordered_map<int, int> freq_map;
        for(int num:nums) ++freq_map[num];
        if(k > freq_map.size()) cout<<"bad parameter k\n";

        // 将频率放进vector中方便随机读取
        for(auto &it: freq_map) freq_list.push_back({it.first, it.second});

        // 前K个元素放进堆空间，进行堆的初始化
        for(int i=0; i<k; ++i) heap.push_back(freq_list[i]);
        for(int i=heap.size()/2-1; i>=0; --i) 
            heapify(heap, i);
        
        // 循环判断剩余元素，大于堆顶则替换掉堆顶然后执行堆化函数
        for(int i=k; i<freq_list.size(); ++i){
            if(freq_list[i][1] > heap[0][1]){
                heap[0] = freq_list[i];
                heapify(heap, 0);
            } 
        }

        // 从堆中获取最终结果
        vector<int> ans;
        for(vector<int> v: heap) ans.push_back(v[0]);
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> nums = {5,3,1,1,1,3,5,73,1};
    Solution * s = new Solution();
    vector<int> ans = s->topKFrequent(nums, 3);
    for(int n: ans) cout<<n<<" ";
    return 0;
}
/*
执行用时：12 ms, 在所有 C++ 提交中击败了83.70% 的用户
内存消耗：14 MB, 在所有 C++ 提交中击败了5.02% 的用户

时间复杂度分析：
遍历原数据花费O(n)
中间若干遍历操作均小于等于O(n)
堆初始化及后续替换堆顶重新初始化都是O(logk)
整体下来时间复杂度为O(nlogk)
*/
#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;


class Solution {
public:
    // void heapify(int heap[], int len, int k){
    //     // heapify the node k
    //     if(len < 2) return;
        
    //     int l = k*2+1;
    //     int r = l+1;

    //     int minimum = min(l, r);
    //     minimum = min(minimum, k);
    //     if(minimum == k) return;

    //     std::swap(heap[k], minimum);
    //     heapify(heap, len, minimum);
    // }

    void sift_up(vector<vector<int>> &heap, int chlid){
        vector<int> val = heap[chlid];
        while (chlid >> 1 > 0 && val[1] < heap[chlid>>1][1]){
            heap[chlid] = heap[chlid>>1];
            chlid >>= 1;
            heap[chlid] = val;
        }
    }

    void sift_down(vector<vector<int>> &heap, int root, int k){
        vector<int> val = heap[root];
        while (root << 1 < k){
            int chlid = root << 1;
            // 注意这里位运算优先级要加括号
            if ((chlid|1) < k && heap[chlid|1][1] < heap[chlid][1]) chlid |= 1;
            if (heap[chlid][1] < val[1]){
                heap[root] = heap[chlid];
                root = chlid;
            }
            else break;
        }
        heap[root] = val;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        vector<vector<int>> heap;
        unordered_map<int, int> counts;
        for(int n:nums) ++counts[n];  // counting nums
        // push all counting results into heap vector
        // here the heap is not a really heap
        heap.push_back({-1,-1});
        for(auto &it: counts) heap.push_back({it.second, it.first});
        
        // heapify the first k items
        for(int i=0; i<k; ++i) sift_up(heap, i-1);
        // handle the remaining items
        for(int i=k; i<heap.size(); ++i){
            if(heap[i][0] > heap[0][0]){
                heap[0] = heap[i];
                sift_down(heap, 1, k+1);
            }
        }

        // int* heap = new int[k]; 
        // for(int i=0; i<k; ++i){
        //     heap[i] = nums[i];
        // }

        // init the heap down-to-top
        // for(int i= k/2-1; i>=0; --i){
        //     heapify(heap, k, i);
        // }
        // for(int i=0; i<k; ++i){
        //     std::cout<<heap[i]<<" ";
        // }
        for(int i=1; i<k+1; ++i) ans.push_back(heap[i][1]);
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> nums = {5,3,1,2,2,3};

    Solution * s = new Solution();
    vector<int> ans = s->topKFrequent(nums, 2);
    for(int n:ans)cout<<n<<" ";
    return 0;
}

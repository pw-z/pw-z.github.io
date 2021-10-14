#include<iostream>
#include<vector>
using namespace std;


class Solution {
public:
    void heapify(int heap[], int len, int k){
        // heapify the node k
        if(len < 2) return;
        
        int l = k*2+1;
        int r = l+1;

        int minimum = min(l, r);
        minimum = min(minimum, k);
        if(minimum == k) return;

        std::swap(heap[k], minimum);
        heapify(heap, len, minimum);
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        int* heap = new int[k]; 
        for(int i=0; i<k; ++i){
            heap[i] = nums[i];
        }

        // init the heap down-to-top
        for(int i= k/2-1; i>=0; --i){
            heapify(heap, k, i);
        }
        for(int i=0; i<k; ++i){
            std::cout<<heap[i]<<" ";
        }

        return ans;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> nums = {5,3,1,2,2,3};

    Solution * s = new Solution();
    s->topKFrequent(nums, 6);
    return 0;
}

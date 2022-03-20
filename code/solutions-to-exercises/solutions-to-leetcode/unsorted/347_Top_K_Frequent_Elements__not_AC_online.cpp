#include<unordered_map>
#include<vector>
#include<iostream>
using std::vector;
using std::unordered_map;
using std::cout;

struct mypair{
    int counts;
    int number;
};

class MinHeap{
    vector<mypair*> heap;
public:
    void replace_top_with(mypair* p){
        heap[0] = p;
        heapify(0);
    }

    mypair* top(){
        return heap[0];
    }

    int get(int i){
        return heap[i]->number;
    }

    // 插入节点
    void insert(int key, int val){
        mypair* p = new mypair;
        p->counts = key;
        p->number = val;
        heap.push_back(p);
    }

    // 将初始数组转化为堆
    void init_heap(){
        // 每个叶节点自成一堆，从第一个有叶节点的节点开始进行堆化
        // cout<<heap.size();
        for(int i=heap.size()/2-1; i>=0; --i){
            heapify(i);
        }
    }

    // 对某个左右子节点均已成堆的节点（序号i）进行堆化操作
    void heapify(int i){
        // 获取左右子节点位置
        int l = 2*i+1;
        int r = l+1;
        // 确定当前节点与其子节点中的最小值
        int min = i;
        if(l<heap.size() && heap[l]->counts < heap[i]->counts) min=l;
        if(r<heap.size() && heap[r]->counts < heap[l]->counts) min=r;
        if(min==i)return;  // 待堆化节点本身是最小的情况下，堆化完成
        // 最小值交换到正确位置
        mypair* temp = heap[i];
        heap[i] = heap[min];
        heap[min] = temp;
        // 被交换下来的节点继续堆化操作
        heapify(min);
    }

};

class Solution1 {
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
    void replace_top_or_not(MinHeap* heap, struct mypair* p){
        if(p->counts > heap->top()->counts){
            heap->replace_top_with(p);
        }
    }
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        unordered_map<int,int> count;
        for(int &num: nums){
            ++count[num];
        }

        MinHeap* myheap = new MinHeap();

        // 用前K个元素初始化最小堆
        int i=0;
        for(auto it: count){
            if(i<k){
                myheap->insert(it.second, it.first);
            }
            ++i;
        }
        myheap->init_heap();

        // 对第K个之后的元素进行处理，看是否需要入堆
        int j=0;
        for(auto it: count){
            if(j>=k){
                mypair* p = new mypair;
                p->counts = it.second;
                p->number = it.first;
                replace_top_or_not(myheap, p);
            }
            ++j;
        }
        
        // 获取最终结果
        for(int i=0; i<k; ++i){
            ans.push_back(myheap->get(i));
        }
        return ans;
    }
};

int main1(){
    // vector<int> nums = {5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3};
    // vector<int> nums = {2,3,4,1,4,0,4,-1,-2,-1};
    vector<int> nums = {5,3,1,1,1,3,5,73,1};
    Solution1* s = new Solution1();
    vector<int> ans = s->topKFrequent(nums, 3);
    for(int num: ans){
        cout<<num<<" ";
    }
    return 0;
}

/****
以上代码提交leetcode，与本地运行结果不符

执行结果：
解答错误
通过测试用例：18 / 21
输入：
[5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]
3
输出：
[3,-1,2]
预期结果：
[3,7,10]
*/

/**
以下代码将外部类定义、变量等全部挪到方法内部

通过测试用例：18 / 21
输入：
[5,3,1,1,1,3,5,73,1]
3
输出：
[3,1,73]
预期结果：
[1,3,5]

仍然不行...本地运行的结果都是对的
 */
class Solution {
public:
    void heapify(vector<mypair*>& heap, int i){
        // 获取左右子节点位置
        int l = 2*i+1;
        int r = l+1;
        // 确定当前节点与其子节点中的最小值
        int min = i;
        if(l<heap.size() && heap[l]->counts < heap[i]->counts) min=l;
        if(r<heap.size() && heap[r]->counts < heap[l]->counts) min=r;
        if(min==i)return;  // 待堆化节点本身是最小的情况下，堆化完成
        // 最小值交换到正确位置
        mypair* temp = heap[i];
        heap[i] = heap[min];
        heap[min] = temp;
        // 被交换下来的节点继续堆化操作
        heapify(heap, min);
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> ans;
        vector<mypair*> heap;

        unordered_map<int,int> count;
        for(int &num: nums){
            ++count[num];
        }

        // 用前K个元素初始化最小堆
        int i=0;
        for(auto it: count){
            if(i<k){
                mypair* p = new mypair;
                p->counts = it.second;
                p->number = it.first;
                heap.push_back(p);
            }else{
                break;
            }
            ++i;
        }
        // 每个叶节点自成一堆，从第一个有叶节点的节点开始进行堆化
        for(int x=heap.size()/2-1; x>=0; --x){
            heapify(heap, x);
        }

        // 对第K个之后的元素进行处理，看是否需要入堆
        int j=0;
        for(auto it: count){
            if(j>=k){
                mypair* p = new mypair;
                p->counts = it.second;
                p->number = it.first;
                if(p->counts > heap[0]->counts){
                    heap[0] = p;
                    heapify(heap, 0);
                }
            }
            ++j;
        }
        
        // 获取最终结果
        for(int x=0; x<k; ++x){
            ans.push_back(heap[x]->number);
        }
        return ans;
    }
};

int main2()
{
    Solution* s = new Solution();
    // vector<int> nums = {2,3,4,1,4,0,4,-1,-2,-1};
    vector<int> nums = {5,3,1,1,1,3,5,73,1};
    vector<int> ans = s->topKFrequent(nums, 3);
    for(int num: ans){
        cout<<num<<" ";
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    main1();
    main2();
    return 0;
}


/*
参考代码阅读：

作者：xxinjiee
链接：https://leetcode-cn.com/problems/top-k-frequent-elements/solution/python-dui-pai-xu-by-xxinjiee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
class SolutionRefer {
public:
    // sift_up 自底向上将堆建立起来，作用相当于上面自己写的init_heap()
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
        unordered_map<int, int> stat;
        for (auto &num : nums) stat[num]++;
        // 这里用vector<int>存储map关系
        vector<vector<int>> vec_stat;
        // 此处使用大括号初始化vector，即{n1, n2} 是一个vector，vector[0]=n1, vector[1]=n2
        for (auto &item : stat) vec_stat.push_back({item.first, item.second});

        // 将前K个元素(用vector表示的map对儿)依次入堆，每次入堆后进行堆化操作
        vector<vector<int>> heap;
        heap.push_back({0, 0});
        for (int i = 0; i < k; i++){
            heap.push_back(vec_stat[i]);
            sift_up(heap, heap.size()-1);
        }

        // 剩余的元素依次与堆顶元素比较，大于则入堆，执行自顶向下的堆化
        for (int i = k; i < vec_stat.size(); i++){
            if (vec_stat[i][1] > heap[1][1]){
                heap[1] = vec_stat[i];
                sift_down(heap, 1, k+1);
            }
        }
        
        vector<int> result;
        for (int i = 1; i < k+1; i++) result.push_back(heap[i][0]);
        return result;
    }
};


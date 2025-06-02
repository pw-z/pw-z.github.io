# 堆的实现及相关应用场景总结

*Posted on 2021.10.17 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*  

- [1. 以小顶堆为例讨论堆的递归非递归等实现思路](#1-以小顶堆为例讨论堆的递归非递归等实现思路)
  - [1.1. 带有详细注释的堆的实现](#11-带有详细注释的堆的实现)
  - [1.2. 对上述代码的测试](#12-对上述代码的测试)
  - [1.3. 对上述代码的讨论](#13-对上述代码的讨论)
- [2. 堆排序总结](#2-堆排序总结)
- [3. TopK问题总结](#3-topk问题总结)
  - [3.1. 思路概述](#31-思路概述)
  - [3.2. 力扣347题解](#32-力扣347题解)
- [4. 堆与栈在内存管理层面上的区分](#4-堆与栈在内存管理层面上的区分)
  - [4.1. 一点碎碎念@堆栈是堆还是栈](#41-一点碎碎念堆栈是堆还是栈)
  - [4.2. 堆与栈在内存管理层面上的区分](#42-堆与栈在内存管理层面上的区分)

## 1. 以小顶堆为例讨论堆的递归非递归等实现思路

### 1.1. 带有详细注释的堆的实现

先看代码，这份小顶堆的实现包含了递归及非递归两种形式，构造函数的第三个参数决定了采用那种形式对堆进行初始化，传零则采用递归的形式，非零则采用非递归的形式，两种形式在效率上会有一定差异，但是结果应该是相同的。

可以不看具体代码，函数方法的实现思路已经非常详细的写在注释中，只读个思路不会影响后文的阅读。

注意这份代码仅考虑了堆元素为正整数的情况，在测试用例中会有体现，实现的宽容度及鲁棒性不是本文的重点。

```c++
#ifndef _HEAP_H_
#define _HEAP_H_

#include<vector>
#include<iostream>
using std::vector;
using std::cout;
using std::endl;

namespace pwz {

class min_heap
{
private:
    /*
    用一个vector来保存堆数据，抽象结构上堆是一颗
    完全二叉树，在本类中规定根节点的下标为0，由完
    全二叉树的性质可以知道：

    对于长度为n的堆，其首个有子节点的节点下标为n/2-1，
    对于下标为i的节点，其左子节点的下标为`2*i+1`，
    对于下标为i的节点，其父节点的下标为(n-1)/2向下取整
    */
    vector<int> heap;
public:
    min_heap();
    ~min_heap();
    min_heap(vector<int> data, int size, int init_type){
        // 按值传参不在原数据上操作，保证类的独立性
        for(int i=0; i<size; ++i){
            heap.push_back(data[i]);
        }
        if(init_type == 0) init_heap_recursive();
        else init_heap_non_recursive();
    }

    /*
    将原始数组初始化为小顶堆，具体递归体见下一方法
    
    思路：
    对于堆顶下标为0的数组，`heap.size()/2-1`为该数组
    首个有子节点的节点，每个叶节点已经成堆，从第一个有
    叶节点的节点开始不断向上调用Heapify函数进行堆化，
    直到堆顶即完毕
    */
    void init_heap_recursive(){
        // cout<<heap.size();
        for(int i=heap.size()/2-1; i>=0; --i){
            heapify_recursive(i);
        }
    }
    /*
    递归进行堆化操作

    思路：
    对某个左右子节点均已成堆的节点（序号idx）进行堆化，
    同理，对于堆顶下标为0的数组，左子节点下标为2*idx+1，
    右子节点为2*idx+2，对于父节点与两个子节点，若当前
    父节点就是最小的节点，则已经完成最小堆的堆化，不然
    则需要将最小的节点与父节点（即cur）交换，交换后子树
    或已经不满足堆的定义，故对相应子树继续（递归）调用
    此过程，直到已经到达叶节点或中途某个父节点满足堆定义
    */
    void heapify_recursive(int idx){
        // 获取左右子节点位置
        int l = 2*idx+1;
        int r = l+1;
        // 确定当前节点与其子节点中的最小值（的节点坐标）
        int min = idx;
        if(l<heap.size() && heap[l] < heap[idx]) min=l;
        if(r<heap.size() && heap[r] < heap[min]) min=r;
        if(min==idx)return;  // 待堆化节点本身是最小的情况下，堆化完成
        // 最小值交换到正确位置
        int temp = heap[idx];
        heap[idx] = heap[min];
        heap[min] = temp;
        // 被交换下来的节点继续堆化操作
        heapify_recursive(min);
    }


    /*
    堆的非递归方法，包括：
        * 初始化堆
        * 将堆顶元素下降到正确位置
        * 将堆末元素上浮到正确位置
    
    初始化过程是不断往堆末添加元素，然后调用上浮函数的过程，
    利用循环来替代递归，避免了系统调用、参数传递等多余开销。
    */
    void init_heap_non_recursive(){
        // 通过同类型vector初始化一个临时vector
        vector<int> temp(heap);
        heap.clear();
        for(int i=0; i<temp.size(); ++i){
            // cout<<"handling "<<temp[i]<<"\n";
            heap.push_back(temp[i]);
            heapify_up(i);
        }
    }
    /*
    在合法的最小堆末尾添加一个新元素之后，将其上浮到正确位置

    父节点的下标为`(idx-1)/2`，右节点多出来的1被除法取整，不
    用进行特殊处理，循环判断当前节点是否小于父节点，小于则与
    父节点进行交换，再向上进行判断，直到不小于或下标减小到0
    */
    void heapify_up(int idx){
        int cur = idx;
        int par = (cur-1)/2;
        while(cur > 0 && heap[cur] < heap[par]){
            int temp = heap[cur];
            heap[cur] = heap[par];
            heap[par] = temp;

            cur = par;
            par = (cur-1)/2;
        }
    }
    /*
    当堆顶被新元素替换后，将其下沉到正确位置

    当前节点（父节点）与子节点不断比较，若大于较小的子节点，则
    与其交换，以交换后的位置继续向下进行比较，直到超出范围或该
    节点就是最小的节点
    */
    void heapify_down(int idx){
        int len = heap.size();
        int cur = idx, l, r, min, temp;
        while (cur < len/2)
        {
            l = cur*2+1;
            r = l+1;
            min = cur;
            if(l < len && heap[l] < heap[cur]) min=l;
            if(r < len && heap[r] < heap[min]) min=r;
            if(min == cur) return;
            
            temp = heap[cur];
            heap[cur] = heap[min];
            heap[min] = temp;

            if(min == l) cur=l;
            else cur=r;
        }
    }


    
    // 工具函数，格式化打印当前堆
    void to_string(){
        for(int i=0; i<heap.size(); ++i) cout<<heap[i]<<" ";
        cout<<endl;
    }
    // 工具函数，替换堆顶元素并重新堆化
    void replace_top_with(int x){
        heap[0] = x;
        heapify_down(0);
    }

};//class min_heap

}//namespace pwz

#endif
```

### 1.2. 对上述代码的测试

用如下测试代码冒了个烟，验证代码基本功能，同时简单对递归与非递归的效率做了个对比，发现非递归的效率更低，理论上来讲非递归实现一般可以比递归实现效率要高一点，但说到底还是取决于具体实现，本文的上述非递归实现实际上是完全另一个思路了，可比性并不强。

```C++
#include<iostream>
#include "my_heap.h"
#include<time.h>

using namespace pwz;
using std::cout;

/*
测试用例的生成：

正序数组：{0,1,2,3,4,5,6,7,8,9,10...},
逆序数组：{999,998,997...},
重复的数：{字面意思},
随机数组：{利用rand函数生成0~999之间的随机数},
极端的长：{元素同随机数组，但长度为传参长度的平方}
*/
void testcase_generator(int len){
    cout<<"正序数组： \n{";
    for(int i=0; i<len-1; ++i) cout<<i<<", ";
    cout<<len-1<<"}\n";

    cout<<"逆序数组： \n{";
    for(int i=len; i>0; --i) cout<<i<<", ";
    cout<<0<<"}\n";

    cout<<"重复的数： \n{";
    for(int i=len; i>0; --i) cout<<1<<", ";
    cout<<1<<"}\n";

    cout<<"随机数组： \n{";
    for(int i=0; i<len-1; ++i) cout<<rand()%999<<", ";
    cout<<rand()%999<<"}\n";


    cout<<"极端的长： \n{";
    int llen = len*len;
    for(int i=0; i<llen; ++i) cout<<rand()%999<<", ";
    cout<<rand()%999<<"}\n";
}


void min_heap_recursive_test(){
    vector<vector<int>> cases = {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49},
        {50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}       ,
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {41, 485, 340, 526, 188, 739, 489, 387, 988, 488, 710, 173, 304, 843, 970, 491, 997, 953, 831, 441, 423, 618, 905, 153, 292, 394, 438, 734, 737, 914, 452, 747, 785, 549, 870, 931, 692, 325, 52, 903, 731, 834, 353, 363, 690, 668, 156, 718, 281, 874}
    };
    for(vector<int> _case: cases){
        min_heap* my_heap = new min_heap(_case, _case.size(), 0);
        my_heap->to_string();
    }
}

void min_heap_non_recursive_test(){
    vector<vector<int>> cases = {
        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49},
        {50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}       ,
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
        {41, 485, 340, 526, 188, 739, 489, 387, 988, 488, 710, 173, 304, 843, 970, 491, 997, 953, 831, 441, 423, 618, 905, 153, 292, 394, 438, 734, 737, 914, 452, 747, 785, 549, 870, 931, 692, 325, 52, 903, 731, 834, 353, 363, 690, 668, 156, 718, 281, 874}
    };
    for(vector<int> _case: cases){
        min_heap* my_heap = new min_heap(_case, _case.size(), 1);
        my_heap->to_string();
    }
}

void performance(){
    vector<int> test_data;
    for(int i=1000000; i>0; --i){
        test_data.push_back(rand()%9999);
    }
    vector<int> test_data2(test_data);
    cout<<&test_data<<"\n"<<&test_data2<<"\n";

    clock_t start,end;
    start = clock();
    min_heap* heap1 = new min_heap(test_data, test_data.size(), 1);
    end = clock();
    cout<<"非递归耗时："<<double(end-start)*1000/CLOCKS_PER_SEC<<" ms\n";


    start = clock();
    min_heap* heap2 = new min_heap(test_data2, test_data2.size(), 0);
    end = clock();
    cout<<"递归耗时："<<double(end-start)*1000/CLOCKS_PER_SEC<<" ms\n";
}
/*
0x62fd50
0x62fd30
非递归耗时：58 ms
递归耗时：43 ms
*/

int main(int argc, char const *argv[])
{
    // testcase_generator(50);

    min_heap_recursive_test();
    min_heap_non_recursive_test();
    // performance();

    return 0;
}
/*
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 
0 4 1 12 5 2 20 16 13 8 6 3 24 22 21 18 17 14 32 10 9 7 28 27 26 25 38 23 37 44 36 19 35 43 34 15 33 42 47 11 31 41 30 49 29 40 46 48 50 39 45 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
41 52 153 325 156 173 452 387 485 353 188 281 304 734 489 491 549 692 526 441 423 363 668 340 292 394 438 843 737 914 970 747 785 997 870 931 953 988 831 903 731 834 488 618 690 710 905 718 739 874 

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 
0 5 1 14 6 2 22 19 15 11 7 3 27 25 23 34 20 18 16 30 12 10 8 26 4 45 28 46 38 39 24 50 41 44 29 47 35 36 17 48 33 42 13 43 31 32 9 49 37 40 21 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
41 52 153 188 156 173 452 491 325 423 353 281 340 734 489 526 549 831 387 488 441 618 363 292 304 394 438 843 737 970 914 747 785 997 870 988 931 953 692 903 731 834 485 710 690 905 668 739 718 874
*/
```


### 1.3. 对上述代码的讨论

这份实现中核心函数方法如下：
* void init_heap_recursive()
* void heapify_recursive(int idx)
* void init_heap_non_recursive()
* void heapify_up(int idx)
* void heapify_down(int idx)

递归初始化过程中，`init_heap_recursive()`从最后一个有叶节点的节点开始向前朝着根结点不断调用递归函数`heapify_recursive(int idx)`，自底向上校正每一个父节点让其成为合法的堆，校正的过程是递归的过程，每一次递归函数则是自顶向下的去处理对应的那个子堆。

非递归初始化过程中，`init_heap_non_recursive()`不断向现有的堆末尾追加一个元素，然后调用`heapify_up(int idx)`将该元素上浮到合法位置。

其实`init_heap_recursive()`加上`heapify_down(int idx)`组合出来的非递归才更能对应于这里的递归思路，这个一会儿TopK问题中会用到，思路重合就没在此处这样写了。

宏观来看，这些函数的功能是一致的，均可以将非法堆合法化，区别一定程度上在于具体堆化的过程是自底向上还是自顶向下，抑或是上下相结合，另外最重要的，选用了其中某个堆化函数，对应的要构建符合其适用的数据环境，如向堆末添加元素然后调用自顶向下的堆化函数，这样是不行的，`heapify_down(int idx)`函数并不能覆盖非法部分处于合法部分后面的情况，自顶向下推进到非法的那颗子树的时候，认为之前的东西都可以不用动了，然后来调整这个非法子树，而实际上这个非法子树调整好后，并不能保证其与整体的关系是否正确。

简而言之每个堆化函数有其适用的条件。无论堆化的过程是怎么样的，最终构建出符合堆结构定义的数据就好，这里的上浮函数、下降函数或者递归函数，不过是利用了完全二叉树的特性而形成的经典堆化思路。利用完全二叉树特性写出来的代码一般大差不差，如果遇到有谁写出来了非常不一样的代码，关注他是怎么描述这个堆化的过程的就好。


## 2. 堆排序总结

堆的结构特性使得建堆仅仅是排序的第一个步骤，这时按序输出堆元素是得不到一个有序序列的，堆结构可以保证的在于，堆顶的那个元素一定是一个最大或最小值，由此堆排序的思路也就有了，不断取得堆顶元素，堆顶元素拿走后将最后一个元素放到堆顶，执行堆化操作，直到堆为空，也就取出来了一份有序序列。

前文的最小堆已经将核心代码实现了，补充上堆排序的架子即可，下面给出伪代码(python)：

```python
def heap_sort(data):
    sorted_data = []
    heap = init_heap_with(data)  # 初始化堆
    for i in range(len(heap)):  # 遍历所有堆元素 O(n)
        sorted_data[i] = heap.pop_top()  # 取出堆顶
        heap[0] = heap[len(heap)-1]  # 将堆尾元素放到堆顶
        heap.pop_back()  # 删除堆尾元素
        heapify_down(heap, 0)  # 执行堆化操作 O(logn)
    return sorted_data
```

## 3. TopK问题总结

### 3.1. 思路概述

此处TopK问题特指海量数据的TopK问题，一般排序算法用快排什么的效率也就到nlogn为止了，但借助一个固定大小的堆，可以进一步将效率提升到nlogk的程度，这里的k就是堆的规模。

思路如下：  
1. 根据取最小还是最大的k个元素，利用前k个元素构建大顶堆或者小顶堆
2. 不断用后续元素与堆顶比较，符合条件则取代堆顶执行堆化函数

堆顶充当了守门员的角色，例如求最大的K个元素，需要用小顶堆，那么堆顶就是符合最大K个元素的最低条件，如果还不如堆顶大，那肯定也不如堆中的其它元素大。同理求最小的K个元素，就需要大顶堆。

由于堆的规模是不变的，每次有符合的元素入堆，堆化函数复杂度仅为logk，整体遍历元素用掉O(n)，所以综合起来的时间复杂度只有nlogk。缺点是什么呢，这个堆本身并不是有序的，只能满足这是最大或最小的k个元素，这k个元素若需要具体排序，那还是要nlogn的，所以数据量较小的情况下用堆并不见得有优势，得是海量数据的TopK问题才适用。

### 3.2. 力扣347题解

题目如下：

>347@Top K Frequent Elements
>
>Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
>
>Example 1:
>* Input: nums = [1,1,1,2,2,3], k = 2
>* Output: [1,2]
>
>Example 2:
>* Input: nums = [1], k = 1
>* Output: [1]
>
>Constraints:  
>    * 1 <= nums.length <= 105  
>    * k is in the range [1, the number of unique elements in the array].  
>    * It is guaranteed that the answer is unique.  
>
>Follow up: Your algorithm's time complexity **must be better than O(n log n)**, where n is the array's size.
>
>来源：力扣（LeetCode）  
>链接：https://leetcode-cn.com/problems/top-k-frequent-elements  
>著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路已经在上面讲完了，这里直接上AC的代码，此份代码正是用了`init_heap_recursive()`加上`heapify_down(int idx)`的组合：

```c++
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
*/
```

## 4. 堆与栈在内存管理层面上的区分

### 4.1. 一点碎碎念@堆栈是堆还是栈

结论是，堆是堆，栈是栈，不存在堆栈这种东西，如果听人这么连起来讲，大半是在说栈。以下是碎碎念，自我梳理。

Photoshop设置成中文模式，可以在图层菜单下的智能对象子菜单中看到一个`堆栈模式`，典型应用是拿来处理星轨照片，可如果把语言切到英文，这里这个`堆栈模式`变成了`Stack Mode`；在翻译软件里输入`堆栈`，翻译出来是`Stack`，用百度翻译输入`堆栈，堆，栈。`，输出是`Stack, stack, stack.`，堆也好栈也好，在中英文对应的过程中有概念重合的地方（一堆东西），可能正因如此才有了堆栈这样一种说法（翻译），单单这样叫并无不妥，只是在面对计算机的另一个名词“堆”的时候，引入了一点混乱。

在数据结构中有堆这种结构，有栈这种结构，在内存管理中，操作系统会维护堆空间，也会维护栈空间，但不论怎样，在基本的计算机科学体系中，并没有“堆栈”这样一种既有堆的特性又有栈的特性的混杂的数据结构或者什么东西。一些约定俗成的叫法亦或是不合理乃至错误的叫法不必过度在意，明确各个名词实质所指就不会混乱，大家理解一致便不会有沟通问题。


### 4.2. 堆与栈在内存管理层面上的区分

自底向上，如网络栈一般，内存管理也分不同的层次，最底层自然是操作系统，往上有编程语言级别的内存管理（例如很多语言的垃圾回收机制），再往上则到了应用程序这一层，也就是程序员的实现。

内存空间的划分一般会有堆空间、栈空间、代码区等概念，具体到堆与栈，栈空间是由操作系统维护的，大小比较有限，负责保存函数执行调用所需要的信息（活动记录），例如函数的返回地址、临时变量等，一个临时变量过期了（如函数调用结束），对应的内存空间会由操作系统自动回收，编写程序时候不必关注。

与栈空间相对应的堆空间，是可以由程序员来自行控制的，在C/C++中即`new`与`delete`或者`melloc`与`free`操控的内存，程序员控制代码如何申请、申请多大的堆空间进行使用以及什么时候将空间释放。如果申请了一块内存忘记释放了，这块儿内存就一直被占用了吗？倒也不会，往底层追溯，进程是操作系统分配资源的基本单位，如今的操作系统大多会按照进程来划分其栈空间、堆空间（受保护内存，如此则在操作系统层面限制了跨进程访问数据这种操作），等到程序退出的时候，操作系统会回收相应进程的资源，这包括那些被泄露的内存。

如此简单区分了堆空间与栈空间，具体到不同操作系统、不同编程语言中，总是有各种具体情况需要讨论，底层的东西还是不通透，有很多疑问没有理清，后续慢慢梳理。



---

相关链接与更多阅读：  
[Leetcode 347 题解 python/c++ 自己实现堆，优先队列](https://leetcode-cn.com/problems/top-k-frequent-elements/solution/python-dui-pai-xu-by-xxinjiee/)  
[为什么 Java 和 JS 等语言需要 VM，不能直接操作内存堆栈空间？ - 向阳的回答 - 知乎](https://www.zhihu.com/question/449995754/answer/1787573395)  
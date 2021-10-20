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
    void heapify_down(){
        int len = heap.size();
        int cur = 0, l, r, min, temp;
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
        heapify_down();
    }

};//class min_heap

}//namespace

#endif
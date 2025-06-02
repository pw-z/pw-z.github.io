# Data Structure from Scratch: Sorting Algorithm

*Posted on 2021.09.05 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

- [1. Complexity & Stability](#1-complexity--stability)
- [2. Header & Namespace](#2-header--namespace)
- [3. Implementation & Test](#3-implementation--test)
  - [3.1. Bubble Sort](#31-bubble-sort)
    - [3.1.1. Impl](#311-impl)
    - [3.1.2. Test](#312-test)
  - [3.2. Selection Sort](#32-selection-sort)
    - [3.2.1. Impl](#321-impl)
    - [3.2.2. Test](#322-test)
  - [3.3. Insertion Sort](#33-insertion-sort)
    - [3.3.1. Impl](#331-impl)
    - [3.3.2. Test](#332-test)
  - [3.4. Shell Sort](#34-shell-sort)
    - [3.4.1. Impl](#341-impl)
    - [3.4.2. Test](#342-test)
  - [3.5. Heap Sort](#35-heap-sort)
    - [3.5.1. Impl](#351-impl)
    - [3.5.2. Test](#352-test)
  - [3.6. Merge Sort](#36-merge-sort)
    - [3.6.1. Impl](#361-impl)
    - [3.6.2. Test](#362-test)
  - [3.7. Quick Sort](#37-quick-sort)
    - [3.7.1. Impl](#371-impl)
    - [3.7.2. Test](#372-test)
  - [3.8. Counting Sort](#38-counting-sort)
    - [3.8.1. Impl](#381-impl)
    - [3.8.2. Test](#382-test)
  - [3.9. Bucket Sort](#39-bucket-sort)
    - [3.9.1. Impl](#391-impl)
    - [3.9.2. Test](#392-test)
  - [3.10. Radix Sort](#310-radix-sort)
    - [3.10.1. Impl](#3101-impl)
    - [3.10.2. Test](#3102-test)
- [4. References & Reviews](#4-references--reviews)

## 1. Complexity & Stability

|Tpye| Algorithm | Best | Worst | Average | Space | Stability | Kernel |
|---|:--- |:---:  |:---: |:---:    |:---:          |:---:   |:---:|
|Comparison
|   |Bubble Sort | n | n^2 |  n^2 | 1 | Yes |Exchanging|
|   |Insertion Sort |  n | n^2 |  n^2 | 1 | Yes |Insertion|
|   |Shell Sort | n log n  | n^2  | depends on gap sequence  | 1  | No |Insertion|
|   |Selection Sort |  n^2 | n^2  | n^2  | 1 | No |Selection|
|   |Heap Sort | n log n  |  n log n |  n log n | 1 | No |Selection|
|   |Merge Sort | n log n |  n log n | n log n  | n | Yes |Merging|
|   |Quick Sort | n log n  |  n^2 |  n log n | n log n | No |Partitioning|
|Non-comparison
|   |Counting Sort | n + k | n + k  |  n + k | n + k  | Yes |Bucket|
|   |Bucket Sort | n + k | n + k  | n + k  | n + k  | Yes |Bucket|
|   |Radix Sort | n * k | n * k  | n * k  | n + k  | Yes |Bucket|


*References:*  
*[https://en.wikipedia.org/wiki/Sorting_algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)*  
*[https://www.programiz.com/dsa/sorting-algorithm](https://www.programiz.com/dsa/sorting-algorithm)*

## 2. Header & Namespace

```c++
// sort.h
#ifndef _SORT_H_
#define _SORT_H_

#include <iostream>

namespace pwz {

void print(int *data, int length){
    for (int i = 0; i < length; i++)
    {
        std::cout<<data[i]<<" ";
    }
    std::cout<<"\n";
}


void bubble_sort(int *data, int length){/*implemention*/}
void selection_sort(int *data, int length){/*implemention*/}
void insertion_sort(int *data, int length){/*implemention*/}
void shell_sort(int* data, int length){/*implemention*/}

void merge_sort__merge(int* data, int left, int right, int* temp){/*implemention*/}
void merge_sort__sort(int* data, int left, int right, int* temp){/*implemention*/}
void merge_sort(int* data, int length){/*implemention*/}

int counting_sort__findmax(int* data, int length){/*implemention*/}
void counting_sort(int* data, int length){/*implemention*/}

int quick_sort__partition(int* data, int length, int low, int high){/*implemention*/}
void quick_sort__sort(int* data, int length, int left, int right){/*implemention*/}
void quick_sort(int* data, int length){/*implemention*/}

void heap_sort__heapify(int* data, int start, int end){/*implemention*/}
void heap_sort(int* data, int length){/*implemention*/}

void bucket_sort__print_buckets(int** bucket, int* bucket_count, 
                                int BUCKET_NUM, int BUCKET_SIZE){/*implemention*/}
void bucket_sort_implementation_my_first_try(int* data, int length){/*implemention*/}
void bucket_sort(int* data, int length){/*implemention*/}

void radix_sort(int* data, int length){/*implemention*/}

} // namespace pwz

#endif
```

## 3. Implementation & Test

### 3.1. Bubble Sort

#### 3.1.1. Impl

```c++

void bubble_sort(int *data, int length){
    int temp;
    for (int i = length-1; i > 1; i--)
    {
        for (int j = 0; j < i; j++)
        {
            if (data[j] > data[j+1])
            {
                temp = data[j+1];
                data[j+1] = data[j];
                data[j] = temp;
            }
        }
    }
}
```

#### 3.1.2. Test

```c++
void bubble_sort_test(){
    std::cout<<"bubble sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    std::cout<<"sort result: ";
    pwz::bubble_sort(data, 20);
    pwz::print(data, 20);
}
/*
bubble sort test:
test data:   2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186 
sort result: -232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
*/

```

### 3.2. Selection Sort

#### 3.2.1. Impl

```c++
void selection_sort(int *data, int length){
    int temp, p_min;
    for (int i = 0; i < length-1; i++)
    {   
        p_min = i;
        for (int j = i+1; j < length; j++)
        {
            if (data[j] < data[p_min])
            {
                p_min = j;
            }
        }
        temp = data[i];
        data[i] = data[p_min];
        data[p_min] = temp;
    }
}
```

#### 3.2.2. Test

```c++
void selection_sort_test(){
    std::cout<<"selection sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    std::cout<<"sort result: ";
    pwz::selection_sort(data, 20);
    pwz::print(data, 20);
}
/*
selection sort test:
test data:   2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
sort result: -232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
*/
```

### 3.3. Insertion Sort

#### 3.3.1. Impl

```c++
void insertion_sort(int *data, int length){
    for (int i = 0; i < length; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (data[j] <= data[j-1]){
                int temp = data[j];
                data[j] = data[j-1];
                data[j-1] = temp;
            }else{
                break;
            }
        }
    }
}
```

#### 3.3.2. Test

```c++
void insertion_sort_test(){
    std::cout<<"insertion sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    pwz::insertion_sort(data, 20);
    std::cout<<"sort result: ";
    pwz::print(data, 20);
}
/*
insertion sort test:
test data:   2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
sort result: -232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
*/
```

### 3.4. Shell Sort

#### 3.4.1. Impl

```c++
void shell_sort(int* data, int length){
    for (int g = length/2; g > 0; g/=2)
    {
        for (int i = g; i < length; i++)
        {
            // !notice the boundary is j>=g, not j>0
            for (int j = i; j >= g; j-=g)
            {
                if (data[j] <= data[j-g])
                {
                    int temp = data[j];
                    data[j] = data[j-g];
                    data[j-g] = temp;
                }else{
                    break;
                }
            }
        }
    }
}
```

#### 3.4.2. Test

```c++
void shell_sort_test(){
    std::cout<<"shell sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    pwz::shell_sort(data, 20);
    std::cout<<"sort result: ";
    pwz::print(data, 20);
}
/*
shell sort test:
test data: 2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186 
sort result: -7 0 0 0 1 2 4 6 7 8 8 9 23 34 34 123 123 186 567 666 
*/
```

### 3.5. Heap Sort

#### 3.5.1. Impl

```c++
void heap_sort__heapify(int* data, int start, int end){
    int current_top = data[start];
    for(int cur = start*2+1; cur <= end; cur=cur*2 +1){
        // print(data, end);
        if (cur < end && data[cur] < data[cur+1]) cur++;
        if (current_top > data[cur]) break;
        data[start] = data[cur];
        start = cur;
    }
    data[start] = current_top;
    // print(data, end);
}
void heap_sort(int* data, int length){
    // std::cout<<"before heap sort: ";
    // print(data, length);
    for(int i = length/2-1; i>=0; --i){  // first node index is 0, not 1
        heap_sort__heapify(data, i, length-1);
    }
    // std::cout<<"heapified: ";
    // print(data, length);
    for(int i=length-1; i>0; --i){
        int temp = data[i];
        data[i] = data[0];
        data[0] = temp;
        // std::cout<<"start sorting, i = "<< i<<"\n";
        // print(data, length);
        // std::cout<<"reheapifing... i = "<< i<<"\n";
        heap_sort__heapify(data, 0, i-1);
        // std::cout<<"heapified... : ";
        // print(data, length);
    }
}
```

#### 3.5.2. Test

```c++
void heap_sort_test()
{
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    int data1[8] = {0,5,5,3,6,7};
    pwz::heap_sort(data, 20);
    pwz::print(data, 20);
    pwz::heap_sort(data1, 6);
    pwz::print(data1, 6);
}
/*
-232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
0 3 5 5 6 7
*/
```

### 3.6. Merge Sort

#### 3.6.1. Impl

```c++
void merge_sort__merge(int* data, int left, int right, int* temp){
    int middle = (left + right)/2;
    std::cout<<"merging...\n";
    std::cout<<left<<" "<<middle<<" "<<right<<"\n";
    int i=left, j=middle+1;
    int cur = 0;
    while (i<=middle && j<=right)
    {
        if (data[i] < data[j])
        {
            temp[cur++] = data[i++];
        }else{
            temp[cur++] = data[j++];
        }

    }
    while (i<=middle)
    {
        temp[cur++] = data[i++];
    }
    while (j<=right)
    {
        temp[cur++] = data[j++];
    }

    cur = 0;
    while (left<=right)
    {
        data[left++] = temp[cur++];
    }
    print(data, 20);
}
void merge_sort__sort(int* data, int left, int right, int* temp){
    if (left < right)
    {
        int middle = (left + right)/2;
        std::cout<<left<<" "<<middle<<" "<<right<<"\n";
        merge_sort__sort(data, left, middle, temp);
        merge_sort__sort(data, middle+1, right, temp);
        merge_sort__merge(data, left, right, temp);
    }
}
void merge_sort(int* data, int length){
    int temp[length];
    merge_sort__sort(data, 0, length-1, temp);
}
```

#### 3.6.2. Test

```c++
void merge_sort_test(){
    std::cout<<"merge sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data: ";
    pwz::print(data, 20);
    pwz::merge_sort(data, 20);
    std::cout<<"sort result: ";
    pwz::print(data, 20);
}
/*
merge sort test:
test data: 2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
0 9 19
0 4 9
0 2 4
0 1 2
0 0 1
merging...
0 0 1
-7 2 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
merging...
0 1 2
-7 2 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
3 3 4
merging...
3 3 4
-7 2 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
merging...
0 2 4
-9 -7 1 2 4 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
5 7 9
5 6 7
5 5 6
merging...
5 5 6
-9 -7 1 2 4 6 7 8 0 9 23 34 123 567 123 666 34 -232 -56 186 
merging...
5 6 7
-9 -7 1 2 4 6 7 8 0 9 23 34 123 567 123 666 34 -232 -56 186
8 8 9
merging...
8 8 9
-9 -7 1 2 4 6 7 8 0 9 23 34 123 567 123 666 34 -232 -56 186
merging...
5 7 9
-9 -7 1 2 4 0 6 7 8 9 23 34 123 567 123 666 34 -232 -56 186
merging...
0 4 9
-9 -7 0 1 2 4 6 7 8 9 23 34 123 567 123 666 34 -232 -56 186
10 14 19
10 12 14
10 11 12
10 10 11
merging...
10 10 11
-9 -7 0 1 2 4 6 7 8 9 23 34 123 567 123 666 34 -232 -56 186
merging...
10 11 12
-9 -7 0 1 2 4 6 7 8 9 23 34 123 567 123 666 34 -232 -56 186
13 13 14
merging...
13 13 14
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 666 34 -232 -56 186 
merging...
10 12 14
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 666 34 -232 -56 186
15 17 19
15 16 17
15 15 16
merging...
15 15 16
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 34 666 -232 -56 186
merging...
15 16 17
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 -232 34 666 -56 186
18 18 19
merging...
18 18 19
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 -232 34 666 -56 186
merging...
15 17 19
-9 -7 0 1 2 4 6 7 8 9 23 34 123 123 567 -232 -56 34 186 666
merging...
10 14 19
-9 -7 0 1 2 4 6 7 8 9 -232 -56 23 34 34 123 123 186 567 666
merging...
0 9 19
-232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666 
sort result: -232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
*/
```

### 3.7. Quick Sort

#### 3.7.1. Impl

```c++
int quick_sort__partition(int* data, int length, int low, int high){
    // pwz::print(data, length);
    // std::cout<<"init  >> low = "<< low<<"  high = "<< high<<"\n";
    int pivot = data[low];
    while (low < high)
    {
        while(low < high && data[high] >= pivot){
            high--;
            // std::cout<<"high-->> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[low] = data[high];
        while (low < high && data[low] <= pivot){
            low++;
            // std::cout<<"low++ >> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[high] = data[low];
    }
    data[low] = pivot;
    // std::cout<<"pivot = "<<low<<"\n";
    return low;
}
void quick_sort__sort(int* data, int length, int left, int right){
    if (left < right)
    {
        int pivot_index = quick_sort__partition(data, length, left, right);
        quick_sort__sort(data, length, left, pivot_index-1);
        quick_sort__sort(data, length, pivot_index+1, right);
    }
}
void quick_sort(int* data, int length){
    quick_sort__sort(data, length, 0, length-1);
}
```

#### 3.7.2. Test

```c++
void quick_sort_test(){
    std::cout<<"quick sort test:\n";
    int data[20] = {2, -7, 4, -9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, -232, -56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    pwz::quick_sort(data, 20);
    std::cout<<"sort result: ";
    pwz::print(data, 20);
}
/*
quick sort test:
test data:   2 -7 4 -9 1 7 6 8 0 9 23 34 123 567 123 666 34 -232 -56 186
sort result: -232 -56 -9 -7 0 1 2 4 6 7 8 9 23 34 34 123 123 186 567 666
*/
```

### 3.8. Counting Sort

#### 3.8.1. Impl

```c++
// counting sort
// only positive numbers supported
int counting_sort__findmax(int* data, int length){
    int max = data[0];
    for (int i = 0; i < length; i++)
    {
        if (data[i] > max)
        {
            max = data[i];
        }    
    }
    return max;
}
void counting_sort(int* data, int length){
    int max = counting_sort__findmax(data, length);
    // std::cout<<"the max: "<<max<<"\n";
    int count[max+1] = {0};
    for (int i = 0; i < length; i++)
    {
        count[data[i]]++;
    }
    for (int i = 0,j = 0; i <= max; i++)
    {
        while (count[i] != 0)
        {
            data[j] = i;
            count[i]--;
            j++;
        }
    }
}
```

#### 3.8.2. Test

```c++
void counting_sort_test(){
    std::cout<<"counting sort test:\n";
    int data[20] = {2, 7, 4, 9, 1, 7, 6, 8, 0, 9,
    23, 34, 123, 567, 123, 666, 34, 232, 56, 186};
    std::cout<<"test data:   ";
    pwz::print(data, 20);
    pwz::counting_sort(data, 20);
    std::cout<<"sort result: ";
    pwz::print(data, 20);
}
/*
counting sort test:
test data:   2 7 4 9 1 7 6 8 0 9 23 34 123 567 123 666 34 232 56 186
sort result: 0 1 2 4 6 7 7 8 9 9 23 34 34 56 123 123 186 232 567 666
*/

```

### 3.9. Bucket Sort

#### 3.9.1. Impl

```c++
int quick_sort__partition(int* data, int length, int low, int high){
    // pwz::print(data, length);
    // std::cout<<"init  >> low = "<< low<<"  high = "<< high<<"\n";
    int pivot = data[low];
    while (low < high)
    {
        while(low < high && data[high] >= pivot){
            high--;
            // std::cout<<"high-->> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[low] = data[high];
        while (low < high && data[low] <= pivot){
            low++;
            // std::cout<<"low++ >> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[high] = data[low];
    }
    data[low] = pivot;
    // std::cout<<"pivot = "<<low<<"\n";
    return low;
}
void quick_sort__sort(int* data, int length, int left, int right){
    if (left < right)
    {
        int pivot_index = quick_sort__partition(data, length, left, right);
        quick_sort__sort(data, length, left, pivot_index-1);
        quick_sort__sort(data, length, pivot_index+1, right);
    }
}
void quick_sort(int* data, int length){
    quick_sort__sort(data, length, 0, length-1);
}

// heap sort
void heap_sort__heapify(int* data, int start, int end){
    int current_top = data[start];
    for(int cur = start*2+1; cur <= end; cur=cur*2 +1){
        // print(data, end);
        if (cur < end && data[cur] < data[cur+1]) cur++;
        if (current_top > data[cur]) break;
        data[start] = data[cur];
        start = cur;
    }
    data[start] = current_top;
    // print(data, end);
}
void heap_sort(int* data, int length){
    // std::cout<<"before heap sort: ";
    // print(data, length);
    for(int i = length/2-1; i>=0; --i){  // first node index is 0, not 1
        heap_sort__heapify(data, i, length-1);
    }
    // std::cout<<"heapified: ";
    // print(data, length);
    for(int i=length-1; i>0; --i){
        int temp = data[i];
        data[i] = data[0];
        data[0] = temp;
        // std::cout<<"start sorting, i = "<< i<<"\n";
        // print(data, length);
        // std::cout<<"reheapifing... i = "<< i<<"\n";
        heap_sort__heapify(data, 0, i-1);
        // std::cout<<"heapified... : ";
        // print(data, length);
    }
}

// bucket sort
void bucket_sort__print_buckets(int** bucket, int* bucket_count, int BUCKET_NUM, int BUCKET_SIZE){
    for (int i = 0; i < BUCKET_NUM; i++)
    {
        std::cout<<"bucket "<<i+1<<" : ";
        for (int j = 0; j < bucket_count[i]; j++)
        {
            std::cout<<*((int*)bucket + i*BUCKET_SIZE + j)<<" ";
        }
        std::cout<<"\n";
    }
}
void bucket_sort_implementation_my_first_try(int* data, int length){
    int BUCKET_NUM = 5;
    int BUCKET_SIZE = 10;
    int bucket[BUCKET_NUM][BUCKET_SIZE];
    int bucket_count[BUCKET_NUM] = {0,};

    // B1-B5 : 20-, 21-40, 41-60, 61-80, 81+
    for (int  i = 0; i < length; i++)
    {
        if(data[i]<21){
            bucket[0][bucket_count[0]++] = data[i];
        }else if (data[i] < 41){
            bucket[1][bucket_count[1]++] = data[i];
        }else if (data[i] < 61){
            bucket[2][bucket_count[2]++] = data[i];
        }else if (data[i] < 81){
            bucket[3][bucket_count[3]++] = data[i];
        }else{
            bucket[4][bucket_count[4]++] = data[i];
        }
    }

    // bucket_sort__print_buckets((int**)bucket, bucket_count, BUCKET_NUM, BUCKET_SIZE);
    int cur = 0;
    for (int i = 0; i < BUCKET_NUM; i++)
    {
        // choice another sort algorithm
        // or keep using bucket_sort
        quick_sort(&bucket[i][0], bucket_count[i]);

        for (int j = 0; j < bucket_count[i]; j++)
        {
            data[cur++] = bucket[i][j];
        }
    }
    // bucket_sort__print_buckets((int**)bucket, bucket_count, BUCKET_NUM, BUCKET_SIZE);
}
// int bucket_sort__floor(double x){
//     if (x < 0)
//         return int(x)-1;
//     else
//         return int(x);
// }
void bucket_sort(int* data, int length){
    int BUCKET_NUM = 5;
    int bucket_capacity = length;
    // bucket_capacity is how many numbers one bucket can take,
    // make bucket_capacity = length is a lazy choice for the
    // worst situation that most of the numbers in the data[] are close or the same.
    std::cout<<"bucket capacity is "<<bucket_capacity<<"\n";

    int max=data[0], min=data[0];
    for (int i = 0; i < length; i++)
    {
        if (data[i] > max){
            max = data[i];
        }else if (data[i] < min){
            min = data[i];
        }
    }
    std::cout<<"the max = "<<max<<" and the min = "<<min<<"\n";

    int bucket_range = (max - min + 1)/BUCKET_NUM;
    if (bucket_range < BUCKET_NUM)
    {
        bucket_range = BUCKET_NUM;  // then every item will be put into bucket[0]
    }
    
    std::cout<<"bucket range = "<<bucket_range<<"\n";
    int bucket[BUCKET_NUM][bucket_capacity];
    int bucket_count[BUCKET_NUM] = {0,};
    // bucket_sortprint_buckets((int**)bucket, bucket_count, BUCKET_NUM, bucket_capacity);

    std::cout<<"start putting numbers into buckets:\n";
    int index;
    for (int i = 0; i < length; i++)
    {
        index = (data[i] - min)/bucket_range;
        std::cout<<"i = "<< i <<", number[i] = "<<data[i]<<", index = "<<index<<"\n";
        bucket[index][bucket_count[index]++] = data[i];
    }

    std::cout<<"befor sorting, buckets:\n";
    bucket_sort__print_buckets((int**)bucket, bucket_count, BUCKET_NUM, bucket_capacity);
    
    int cur = 0;
    for (int i = 0; i < BUCKET_NUM; i++)
    {
        // choice another sort algorithm
        // or keep using bucket_sort
        quick_sort(&bucket[i][0], bucket_count[i]);

        for (int j = 0; j < bucket_count[i]; j++)
        {
            data[cur++] = bucket[i][j];
        }
    }
    std::cout<<"after sorting, buckets:\n";
    bucket_sort__print_buckets((int**)bucket, bucket_count, BUCKET_NUM, bucket_capacity);
    
}
```

#### 3.9.2. Test

```c++
void bucket_sort_test(){
    int data1[20] = {0,11,21,31,41,51,61,71,81,91,2,12,22,32,42,52,62,72,82,99};
    pwz::bucket_sort(data1, 20);
    pwz::print(data1, 20);

    std::cout<<"\n\n";

    int data2[20] = {0};
    pwz::bucket_sort(data2, 20);
    pwz::print(data2, 20);
}
/*
bucket capacity is 20
the max = 99 and the min = 0
bucket range = 20
start putting numbers into buckets:
i = 0, number[i] = 0, index = 0
i = 1, number[i] = 11, index = 0
i = 2, number[i] = 21, index = 1
i = 3, number[i] = 31, index = 1
i = 4, number[i] = 41, index = 2
i = 5, number[i] = 51, index = 2
i = 6, number[i] = 61, index = 3
i = 7, number[i] = 71, index = 3
i = 8, number[i] = 81, index = 4
i = 9, number[i] = 91, index = 4
i = 10, number[i] = 2, index = 0
i = 11, number[i] = 12, index = 0
i = 12, number[i] = 22, index = 1
i = 13, number[i] = 32, index = 1
i = 14, number[i] = 42, index = 2
i = 15, number[i] = 52, index = 2
i = 16, number[i] = 62, index = 3
i = 17, number[i] = 72, index = 3
i = 18, number[i] = 82, index = 4
i = 19, number[i] = 99, index = 4
befor sorting, buckets:
bucket 1 : 0 11 2 12
bucket 2 : 21 31 22 32
bucket 3 : 41 51 42 52
bucket 4 : 61 71 62 72
bucket 5 : 81 91 82 99
after sorting, buckets:
bucket 1 : 0 2 11 12
bucket 2 : 21 22 31 32
bucket 3 : 41 42 51 52
bucket 4 : 61 62 71 72
bucket 5 : 81 82 91 99
0 2 11 12 21 22 31 32 41 42 51 52 61 62 71 72 81 82 91 99 


bucket capacity is 20
the max = 0 and the min = 0
bucket range = 5
start putting numbers into buckets:
i = 0, number[i] = 0, index = 0
i = 1, number[i] = 0, index = 0
i = 2, number[i] = 0, index = 0
i = 3, number[i] = 0, index = 0
i = 4, number[i] = 0, index = 0
i = 5, number[i] = 0, index = 0
i = 6, number[i] = 0, index = 0
i = 7, number[i] = 0, index = 0
i = 8, number[i] = 0, index = 0
i = 9, number[i] = 0, index = 0
i = 10, number[i] = 0, index = 0
i = 11, number[i] = 0, index = 0
i = 12, number[i] = 0, index = 0
i = 13, number[i] = 0, index = 0
i = 14, number[i] = 0, index = 0
i = 15, number[i] = 0, index = 0
i = 16, number[i] = 0, index = 0
i = 17, number[i] = 0, index = 0
i = 18, number[i] = 0, index = 0
i = 19, number[i] = 0, index = 0
befor sorting, buckets:
bucket 1 : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
after sorting, buckets:
bucket 1 : 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
*/
```

### 3.10. Radix Sort

#### 3.10.1. Impl

```c++
void radix_sort(int* data, int length){

    // find the max
    int max = data[0];
    for (int i = 0; i < length; i++){
        if (data[i] > max){
            max = data[i];
        }
    }
    std::cout<<"max: "<< max << "\n";

    // caculate the bit width
    int width = 1;
    while (max >= 10)
    {
        ++width;
        max /= 10;
    }
    std::cout<<"width: "<< width << "\n";
    std::cout<<"start sorting...\n";

    // start sorting
    // 19 buckets for both negative and positive numbers
    // number -9 -8 -7 -6 -5 -4 -3 -2 -1  0 1  2  3  4  5  6  7  8  9
    // bucket 0  1  2  3  4  5  6  7  8   9 10 11 12 13 14 15 16 17 18
    int bucket[19][length];
    for (int i=0, base=1; i < width; i++, base*=10){
        int bucket_count[20] = {0};

        // put the datas into buckets
        for (int j = 0; j < length; j++){
            int index = (data[j]/base) % 10 + 9;  // data[j] belongs to bucket[index]
            // std::cout<<data[j]<<" belongs to bucket "<< index<<"\n";
            bucket[index][bucket_count[index]++] = data[j];
        }
        std::cout<<"buckets status "<< i+1 <<":\n";
        bucket_sort__print_buckets((int**)bucket, bucket_count, 19, length);

        // put the datas back
        // j for bucket[j][]
        // k for data[k], k should be 'length' finally.
        // count for bucket[][count] & FIFO.
        for (int j=0, k=0; j < 19; j++){
            int count = 0;
            while (count < bucket_count[j])
            {
                data[k] = bucket[j][count++];
                k++;
            }
        }
        std::cout<<"data status "<< i+1 <<":";
        print(data, length);
    }
}
```

#### 3.10.2. Test

```c++
void radix_sort_test(){
    int data[20] = {0,11,22,33,44,55,66,77,88,98,2,12,23,34,45,56,69,72,81,99};
    std::cout<<"test data1[]:";
    pwz::print(data, 20);
    pwz::radix_sort(data, 20);
    std::cout<<"final result:";
    pwz::print(data, 20);


    int data2[30] = {9876, 777, 66, 456, 456, 123, 234, 111, 666, 2,
                     -91, -82, -73, -64, -55, -46, -37, -28, -19, 0,
                     1, 2, 4, 6, 51, 34, 657, 23, 1111, 10   };
    std::cout<<"\n------------\ntest data2[]:";
    pwz::print(data2, 30);
    pwz::radix_sort(data2, 30);
    std::cout<<"final result:";
    pwz::print(data2, 30);
}
/*
test data1[]:0 11 22 33 44 55 66 77 88 98 2 12 23 34 45 56 69 72 81 99 
max: 99
width: 2
start sorting...
buckets status 1:
bucket 1 :
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
bucket 6 :
bucket 7 :
bucket 8 :
bucket 9 :
bucket 10 : 0
bucket 11 : 11 81
bucket 12 : 22 2 12 72
bucket 13 : 33 23
bucket 14 : 44 34
bucket 15 : 55 45
bucket 16 : 66 56
bucket 17 : 77
bucket 18 : 88 98
bucket 19 : 69 99
data status 1:0 11 81 22 2 12 72 33 23 44 34 55 45 66 56 77 88 98 69 99
buckets status 2:
bucket 1 :
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
bucket 6 :
bucket 7 :
bucket 8 :
bucket 9 :
bucket 10 : 0 2
bucket 11 : 11 12
bucket 12 : 22 23
bucket 13 : 33 34 
bucket 14 : 44 45
bucket 15 : 55 56
bucket 16 : 66 69
bucket 17 : 72 77
bucket 18 : 81 88
bucket 19 : 98 99
data status 2:0 2 11 12 22 23 33 34 44 45 55 56 66 69 72 77 81 88 98 99
final result:0 2 11 12 22 23 33 34 44 45 55 56 66 69 72 77 81 88 98 99

------------
test data2[]:9876 777 66 456 456 123 234 111 666 2 -91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 4 6 51 34 657 23 1111 10
max: 9876
width: 4
start sorting...
buckets status 1:
bucket 1 : -19
bucket 2 : -28
bucket 3 : -37
bucket 4 : -46
bucket 5 : -55
bucket 6 : -64
bucket 7 : -73
bucket 8 : -82
bucket 9 : -91
bucket 10 : 0 10
bucket 11 : 111 1 51 1111
bucket 12 : 2 2
bucket 13 : 123 23
bucket 14 : 234 4 34 
bucket 15 :
bucket 16 : 9876 66 456 456 666 6
bucket 17 : 777 657
bucket 18 :
bucket 19 :
data status 1:-19 -28 -37 -46 -55 -64 -73 -82 -91 0 10 111 1 51 1111 2 2 123 23 234 4 34 9876 66 456 456 666 6 777 657
buckets status 2:
bucket 1 : -91
bucket 2 : -82
bucket 3 : -73
bucket 4 : -64
bucket 5 : -55
bucket 6 : -46
bucket 7 : -37
bucket 8 : -28
bucket 9 : -19
bucket 10 : 0 1 2 2 4 6
bucket 11 : 10 111 1111
bucket 12 : 123 23
bucket 13 : 234 34
bucket 14 :
bucket 15 : 51 456 456 657
bucket 16 : 66 666
bucket 17 : 9876 777
bucket 18 :
bucket 19 :
data status 2:-91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 111 1111 123 23 234 34 51 456 456 657 66 666 9876 777 
buckets status 3:
bucket 1 :
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
bucket 6 :
bucket 7 :
bucket 8 :
bucket 9 :
bucket 10 : -91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 23 34 51 66
bucket 11 : 111 1111 123
bucket 12 : 234
bucket 13 :
bucket 14 : 456 456
bucket 15 :
bucket 16 : 657 666
bucket 17 : 777
bucket 18 : 9876
bucket 19 :
data status 3:-91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 23 34 51 66 111 1111 123 234 456 456 657 666 777 9876
buckets status 4:
bucket 1 :
bucket 2 :
bucket 3 :
bucket 4 :
bucket 5 :
bucket 6 :
bucket 7 :
bucket 8 : 
bucket 9 :
bucket 10 : -91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 23 34 51 66 111 123 234 456 456 657 666 777
bucket 11 : 1111
bucket 12 :
bucket 13 :
bucket 14 :
bucket 15 :
bucket 16 :
bucket 17 :
bucket 18 :
bucket 19 : 9876
data status 4:-91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 23 34 51 66 111 123 234 456 456 657 666 777 1111 9876
final result:-91 -82 -73 -64 -55 -46 -37 -28 -19 0 1 2 2 4 6 10 23 34 51 66 111 123 234 456 456 657 666 777 1111 9876
*/
```

## 4. References & Reviews

* [**https://en.wikipedia.org/wiki/Sorting_algorithm**](https://en.wikipedia.org/wiki/Sorting_algorithm)
* [**https://www.programiz.com/dsa/sorting-algorithm**](https://www.programiz.com/dsa/sorting-algorithm)
* [https://www.runoob.com/w3cnote/ten-sorting-algorithm.html](https://www.runoob.com/w3cnote/ten-sorting-algorithm.html)
* [https://www.cnblogs.com/onepixel/articles/7674659.html](https://www.cnblogs.com/onepixel/articles/7674659.html)
* [https://www.cnblogs.com/chengxiao/p/6194356.html](https://www.cnblogs.com/chengxiao/p/6194356.html)
* [https://zhuanlan.zhihu.com/p/137703433](https://zhuanlan.zhihu.com/p/137703433)
* [http://www.nowamagic.net/librarys/veda/detail/1194](http://www.nowamagic.net/librarys/veda/detail/1194)
* [**https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm**](https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm)
* [**https://blog.csdn.net/qq_41765114/article/details/86435110**](https://blog.csdn.net/qq_41765114/article/details/86435110)
* [https://www.cnblogs.com/nullzx/p/5880191.html](https://www.cnblogs.com/nullzx/p/5880191.html)
* [https://www.cnblogs.com/mengdd/archive/2012/11/30/2796845.html](https://www.cnblogs.com/mengdd/archive/2012/11/30/2796845.html)
* [https://www.geeksforgeeks.org/shellsort/](https://www.geeksforgeeks.org/shellsort/)
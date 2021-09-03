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

void shell_sort(int* data, int length){
    for (int g = length/2; g > 0; g/=2)
    {
        for (int i = g; i < length; i++)
        {
            for (int j = i; j > 0; j-=g)
            {
                if (data[j] < data[j-g])
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

// merge sort
void merge_sort__merge(int* data, int left, int right, int* temp){
    int middle = (left + right)/2;
    std::cout<<"merging...\n";
    std::cout<<left<<" "<<middle<<" "<<right<<"\n";
    int i=left, j=middle+1;
    int cur = 0;
    while (i<=middle, j<=right)
    {
        if (data[i] < data[j])
        {
            temp[cur++] = data[i++];
        }else{
            temp[cur++] = data[j++];
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
    }
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

// counting sort
int counting_sort__findmax(int* data, int length){
    int max;
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
    int count[max] = {0};
    for (int i = 0; i < length; i++)
    {
        count[data[i]]++;
    }
    for (int i = 0,j = 0; i < max; i++)
    {
        while (count[i] != 0)
        {
            data[j] = i;
            count[i]--;
            j++;
        }
    }   
}

// quick sort
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
void bucket_sortprint_buckets(int** bucket, int* bucket_count, int BUCKET_NUM, int BUCKET_SIZE){
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

    // bucket_sortprint_buckets((int**)bucket, bucket_count, BUCKET_NUM, BUCKET_SIZE);
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
    // bucket_sortprint_buckets((int**)bucket, bucket_count, BUCKET_NUM, BUCKET_SIZE);
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
    bucket_sortprint_buckets((int**)bucket, bucket_count, BUCKET_NUM, bucket_capacity);
    
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
    bucket_sortprint_buckets((int**)bucket, bucket_count, BUCKET_NUM, bucket_capacity);
    
}


// radix_sort


} // namespace pwz



#endif
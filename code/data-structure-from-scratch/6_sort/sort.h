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


// counting_sort
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


int quick_sort__partition(int* data, int length, int low, int high){
    pwz::print(data, length);
    std::cout<<"init  >> low = "<< low<<"  high = "<< high<<"\n";
    int pivot = data[low];
    while (low < high)
    {
        while(low < high && data[high] >= pivot){
            high--;
            std::cout<<"high-->> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[low] = data[high];
        while (low < high && data[low] <= pivot){
            low++;
            std::cout<<"low++ >> low = "<< low<<"  high = "<< high<<"\n";
        }
        data[high] = data[low];
    }
    data[low] = pivot;
    std::cout<<"pivot = "<<low<<"\n";
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



} // namespace pwz



#endif
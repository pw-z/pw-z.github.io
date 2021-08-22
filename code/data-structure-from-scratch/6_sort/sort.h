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





void test_sort(int *data){
    //数组作为函数参数传递后，退化为指针
    std::cout<<sizeof(data)<<"\n";
    
    std::cout<<sizeof(data[0])<<"\n";
    int size = sizeof(data) / sizeof(data[0]);
    std::cout<<"length = "<<size<<"\n";
}


}



#endif
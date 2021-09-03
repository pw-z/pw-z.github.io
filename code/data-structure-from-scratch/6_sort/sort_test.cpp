#include "sort.h"
#include <iostream>


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

void heap_sort_test()
{
    int data[10] = {2, 3, 4, 5, 1, 7, 6, 8, 0, 9};
    // pwz::print(data, 10);

    // pwz::bubble_sort(data, 10);
    // pwz::print(data, 10);
    // pwz::selection_sort(data, 10);
    // pwz::print(data, 10);
    // pwz::insertion_sort(data, 10);
    // pwz::print(data, 10);
    // pwz::shell_sort(data, 10);
    // pwz::print(data, 10);
    // pwz::counting_sort(data, 10);
    // pwz::print(data, 10);
    int data1[8] = {0,5,5,3,6,7};
    // pwz::print(data1, 8);
    // pwz::merge_sort(data, 10);
    // pwz::quick_sort(data, 10);
    // pwz::print(data, 10);
    // pwz::quick_sort(data1, 6);
    pwz::heap_sort(data, 10);
    pwz::print(data, 10);
    pwz::heap_sort(data1, 6);
    pwz::print(data1, 6);
}

int main(int argc, char const *argv[])
{
    bucket_sort_test();
    return 0;
}

#include "sort.h"
#include <iostream>


void bucket_sort_test(){
    int data[20] = {1,11,21,31,41,51,61,71,81,91,2,12,22,32,42,52,62,72,82,92};
    pwz::bucket_sort(data, 20);
}

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

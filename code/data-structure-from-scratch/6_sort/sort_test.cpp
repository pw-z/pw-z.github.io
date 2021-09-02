#include "sort.h"
#include <iostream>

int main(int argc, char const *argv[])
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
    return 0;
}
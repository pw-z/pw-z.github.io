#include "sort.h"
#include <iostream>

int main(int argc, char const *argv[])
{
    int data[10] = {2, 3, 4, 5, 1, 7, 6, 8, 0, 9};
    pwz::print(data, 10);

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
    int data1[8] = {0,1,2,3,4,5,6,7};
    // pwz::print(data1, 8);
    pwz::merge_sort(data, 10);
    pwz::print(data, 10);
    return 0;
}





/**
int test1(int argc, char const *argv[])
{
    int data[5] = {2, 3, 4, 5,1};
    std::cout<<sizeof(data)<<"\n";
    std::cout<<sizeof(data[0])<<"\n";
    for (int i = 0; i < 5; i++)
    {
        std::cout<<data[i]<<" ";
    }
    std::cout<<"\n";

    pwz::test_sort(data);
    for (int i = 0; i < 5; i++)
    {
        std::cout<<data[i]<<" ";
    }

    return 0;
}
*/

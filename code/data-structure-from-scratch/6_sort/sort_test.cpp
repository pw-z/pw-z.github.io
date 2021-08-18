#include "sort.h"
#include <iostream>

int main(int argc, char const *argv[])
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

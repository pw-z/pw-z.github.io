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

int main(int argc, char const *argv[])
{
    // bucket_sort_test();
    radix_sort_test();
    return 0;
}

#include<iostream>
#include "my_heap.h"

using namespace pwz;
using std::cout;

/* heap sort test cases
{1, 2, 3, 4}
{4, 3, 2, 1}
{9, 0, 0, 0, 1, 1, 2}
{1, 1, 1, 1, 1}
{123, 345, 567, 1232, 45, 90}
*/

void min_heap_recursive_test(){
    vector<vector<int>> cases = {
        {6, 2, 3, 4},
        {4, 3, 2, 1},
        {9, 0, 0, 0, 1, 1, 2},
        {1, 1, 1, 1, 1},
        {123, 345, 567, 1232, 45, 90}
    };
    for(vector<int> _case: cases){
        min_heap* my_heap = new min_heap(_case, _case.size(), 0);
        my_heap->to_string();
    }
}

void min_heap_non_recursive_test(){
    vector<vector<int>> cases = {
        {6, 2, 3, 4},
        {4, 3, 2, 1},
        {9, 0, 0, 0, 1, 1, 2},
        {1, 1, 1, 1, 1},
        {123, 345, 567, 1232, 45, 90}
    };
    for(vector<int> _case: cases){
        min_heap* my_heap = new min_heap(_case, _case.size(), 1);
        my_heap->to_string();
        my_heap->replace_top_with(9999);
        my_heap->to_string();
    }
}

int main(int argc, char const *argv[])
{
    min_heap_recursive_test();
    cout<<"\n======================\n";
    min_heap_non_recursive_test();

    // vector<int> temp = {1,2,3};
    // cout<<temp.size()<<endl;
    // temp.clear();
    // cout<<temp.size();
    // cout<<(-1)/2;

    return 0;
}
/*
2 4 3 6 
1 3 2 4
0 0 0 9 1 1 2
1 1 1 1 1
45 123 90 1232 345 567

======================
2 4 3 6
3 4 9999 6
1 2 3 4
2 4 3 9999
0 0 0 9 1 1 2
0 1 0 9 9999 1 2
1 1 1 1 1
1 1 1 9999 1
45 123 90 1232 345 567
90 123 567 1232 345 9999
*/
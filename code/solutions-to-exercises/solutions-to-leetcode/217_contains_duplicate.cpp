#include <vector>
#include <iostream>
#include <algorithm>

using std::vector;
using std::cout;
using std::sort;

// time:O(n^2)  too slow
bool containsDuplicate_1(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i+1; j < nums.size(); j++)
        {
            if (nums[i] == nums[j])
            {
                return true;
            }
        }
    }
    return false;
}

// ~ n log n
bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size()-1; i++)
    {
        if (nums[i] == nums[i+1])
        {
            return true;
        }
    }
    return false;
}


void test1(){
    vector<int> test_data {1,2,3,4,5,6,7,8,9,0,9};
    cout<<containsDuplicate(test_data);
}

int main(int argc, char const *argv[])
{
    test1();
    return 0;
}

#include <iostream>
#include <vector>

using namespace std;

// time:O(n^2)  space:O(1)
vector<int> twoSum(vector<int>& nums, int target){
    // cout<<"handling..."<<"\n";
    vector<int> result;
    for (int i = 0; i < nums.size(); i++)
    {
        // cout<<nums[i]<<"\n";
        for (int j = i+1; j < nums.size(); j++)
        {
            if(nums[i] + nums[j] == target){
                result.push_back(i);
                result.push_back(j);
                break;
            }
        }
    }
    return result;
}

// time:O(N)  space:O(N)  --hashmap
vector<int> twoSum_hashmap(vector<int>& nums, int target) {
        unordered_map<int,int> hashmap;
        vector<int> result;
        for(int i = 0; i < nums.size() ; ++i){
            if(hashmap.count(target - nums[i])){
                result.push_back(hashmap[target-nums[i]]);
                result.push_back(i);
                break;
            }
            hashmap.insert(make_pair(nums[i], i));
        }
        return result;
}

int main(int argc, char const *argv[])
{
    vector<int> input = {2, 7, 11, 15};

    vector<int>::iterator it;
    cout<<"your input: ";
    for(it = input.begin(); it!= input.end(); it++){
        cout<<*it<<" ";
    }
    cout<<endl;
    vector<int> result = twoSum(input, 9);
    cout<<"result vector is: ";
    for(it = result.begin(); it != result.end(); ++it){
        cout<<*it<<" ";
    }


    return 0;
}

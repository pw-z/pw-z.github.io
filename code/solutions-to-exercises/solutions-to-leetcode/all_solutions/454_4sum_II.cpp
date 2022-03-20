class Solution {
public:
    // O(n^4) 超时
    // int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
    //     unordered_set<string> set;
    //     for(int i=0; i<nums1.size(); ++i){
    //         for(int j=0; j<nums2.size(); ++j){
    //             for(int k=0; k<nums3.size(); ++k){
    //                 for(int l=0; l<nums4.size(); ++l){
    //                     // cout<<i<<j<<k<<l<<endl;
    //                     // cout<<nums1[i]<<nums2[j]<<nums3[k]<<nums4[l]<<endl;
    //                     if((nums1[i] + nums2[j] + nums3[k] + nums4[l]) == 0){
    //                         string x = to_string(i) + to_string(j) + to_string(k) + to_string(l);
    //                         if(!set.count(x)){
    //                             set.insert(x);
    //                         }
    //                     }
    //                 }
    //             }
    //         }
    //     }
    //     return set.size();
    // }

    // O(n^2) 超时
    // int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
    //     unordered_set<string> set;
    //     unordered_map<string, int> map1;
    //     unordered_map<string, int> map2;
    //     for(int i=0; i<nums1.size(); ++i){
    //         for(int j=0; j<nums2.size(); ++j){
    //             string ij = to_string(i) + to_string(j);
    //             map1[ij] = nums1[i] + nums2[j];
    //         }
    //     }
    //     for(int i=0; i<nums3.size(); ++i){
    //         for(int j=0; j<nums4.size(); ++j){
    //             string ij = to_string(i) + to_string(j);
    //             map2[ij] = nums3[i] + nums4[j];
    //         }
    //     }
    //     for(auto it1=map1.begin(); it1!=map1.end(); ++it1){
    //         for(auto it2=map2.begin(); it2!=map2.end(); ++it2){
    //             if((it1->second + it2->second )== 0){
    //                 // cout<<it1->second<<"  "<<it2->second<<endl;
    //                 string x = it1->first + it2->first;
    //                 // cout<<x<<endl;
    //                 if(!set.count(x)){
    //                     set.insert(x);
    //                 }
    //             }
    //         }
    //     }
    //     return set.size();
    // }

    // O(N^2) 优化后AC
    // 执行用时：244 ms, 在所有 C++ 提交中击败了28.61% 的用户
    // 内存消耗：23.7 MB, 在所有 C++ 提交中击败了55.21% 的用户
    // int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
    //     int result=0;
    //     unordered_map<int, int> map;
    //     for(int i=0; i<nums1.size(); ++i){
    //         for(int j=0; j<nums2.size(); ++j){
    //             ++map[nums1[i] + nums2[j]];
    //         }
    //     }
    //     for(int i=0; i<nums3.size(); ++i){
    //         for(int j=0; j<nums4.size(); ++j){
    //             if(map.count(-nums3[i]-nums4[j])){
    //                 result += map[-nums3[i]-nums4[j]];
    //             }
    //         }
    //     }
    //     return result;
    // }

    // for改为foreach，同时移除map命中判断（未命中的map地址默认值为0）
    // 执行用时：156 ms, 在所有 C++ 提交中击败了96.52% 的用户
    // 内存消耗：23.9 MB, 在所有 C++ 提交中击败了20.49% 的用户
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4){
        int result=0;
        unordered_map<int, int> map;
        for(int i: nums1){
            for(int j: nums2){
                ++map[i+j];
            }
        }
        for(int i: nums3){
            for(int j: nums4){
                result += map[-i-j];
            }
        }
        return result;
    }

};
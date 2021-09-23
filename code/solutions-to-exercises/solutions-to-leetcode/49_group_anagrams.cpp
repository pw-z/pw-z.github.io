class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        for(string s: strs){
            string ss = s;
            sort(s.begin(), s.end());
            hashmap[s].push_back(ss);
        }
        vector<vector<string>> result;
        for(auto it = hashmap.begin(); it != hashmap.end(); ++it){
            result.push_back(it->second);
        }
        return result;
    }
};
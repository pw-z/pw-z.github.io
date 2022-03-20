class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> ans;
        vector<vector<string>> result;
        for(string s: strings){
            char head = s[0];
            string ss = s;
            for(int i=0; i< s.length(); ++i){
                int temp = (int)s[i] - (int)head;
                s[i] = ((char)temp + '0' + 26) % 26;
            }
            ans[s].push_back(ss);
        }
        for(auto key: ans){
            result.push_back(key.second);
        }
        return result;
    }
};
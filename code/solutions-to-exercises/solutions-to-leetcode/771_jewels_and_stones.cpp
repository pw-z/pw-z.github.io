class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int ans=0;
        unordered_set<char> jewels_set;
        for(char c: jewels){
            jewels_set.insert(c);
        }
        for(char c: stones){
            if(jewels_set.count(c)){
                ++ans;
            }
        }
        return ans;
    }
};
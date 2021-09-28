class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max=0;
        int temp_max = 0;
        // 标记上一个重复字符的位置，map中小于此索引的记录是无效的
        int last_dup_loc = -1;
        unordered_map<char, int> map;
        for(int i=0; i<s.length();++i){
            char c = s[i];
            if(map.count(c) && map[c] > last_dup_loc){
                max = max > temp_max? max: temp_max;
                temp_max = i - map[c];
                last_dup_loc = map[c];
            }else{
                ++temp_max;
            }
            map[c] = i;
        }
        // 最后一次命中哈希表之后，没有再发现重复字符，则temp_max需要在此处理
        max = max > temp_max? max: temp_max;
        return max;
    }
};
/*
执行用时：12 ms, 在所有 C++ 提交中击败了79.20% 的用户
内存消耗：8.1 MB, 在所有 C++ 提交中击败了66.76% 的用户

备忘：
一趟遍历出结果，时间复杂度O(N)，
temp_max动态标记着当前的子字符串长度，
利用哈希表不断检查下一个字符是否在前面有重复，
重复了，则前面那个字符及其之前的字符都无效（map.count(c) && map[c] > last_dup_loc），
以所命中字符的下一个字符作为新的子字符串的起点（temp_max = i - map[c];）
*/
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf4);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    int read(char *buf, int n) {
        char* buf4 = new char[4];
        int cur = 0, count=0;
        for(int i=0; i<(n/4); ++i){
            count = read4(buf4);
            for(int j=0; j<count; ++j){
                buf[cur++] = buf4[j];
            }
        }
        
        count = read4(buf4);
        for(int j=0; j<count && j<(n%4); ++j){
            buf[cur++] = buf4[j];
        }
        return cur;
    }
};

/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：6.1 MB, 在所有 C++ 提交中击败了62.62% 的用户
通过测试用例：46 / 46
*/
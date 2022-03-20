/* 题目示例：
Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/hash-table/xh1k9i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

#include<vector>
#include<unordered_set>
#include<iostream>
using std::vector;
using std::unordered_set;
using std::cout;

void process(int n, int d){
    int temp = n;
    int result = 0;
    int depth = d;

    cout<<temp%10<<"^2";
    result += (temp%10)*(temp%10);
    temp /= 10;
    while (temp >= 1)
    {
        cout<<" + "<<temp%10<<"^2";
        result += (temp%10)*(temp%10);
        temp /= 10;
    }
    cout<<" = "<<result<<"\n";
    if (result != 1 && depth < 20)
    {
        process(result, ++depth);
    }
}

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> hashset;
        while (n != 1)
        {
            int result = 0;
            while(n >= 1){
                result += (n%10)*(n%10);
                n /= 10;
            }

            if(hashset.count(result) > 0){
                return false;
            }else{
                n = result;
                hashset.insert(n);
            }
        }
        return true;
    }

    int get_next(int n){
        int sum = 0;
        while (n > 0)
        {
            sum += (n%10) * (n%10);
            n /= 10;
        }
        return sum;
    }
    
    bool isHappy2(int n){
        int p_slow = n;
        int p_fast = get_next(n);
        while (p_fast != 1)
        {
            if (p_fast == p_slow)
            {
                return false;
            }
            
            p_slow = get_next(p_slow);
            p_fast = get_next(get_next(p_fast));
            
        }
        return true;
    }
};

int main(int argc, char const *argv[])
{
    Solution* obj = new Solution();

    int order = 0;
    std::cin>>order;
    while (order != -1)
    {
        // process(order, 1);
        bool res = obj->isHappy2(order);
        std::cout<<res<<"\n";
        std::cin>>order;
    }
    
    return 0;
}

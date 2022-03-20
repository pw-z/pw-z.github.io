#include<iostream>
using std::cout;

class Solution {
public:
    // int reverse(int x) {
    //     int tmp = x>0? x: -x;
    //     int x_bits=0;
    //     for(; tmp>0; tmp/=10){
    //         ++x_bits;
    //     }
    //     // cout<<x_bits<<"\n";

    //     int ans=0;
    //     tmp = x>0? x: -x;
    //     for(;x_bits>0;--x_bits){
    //         if(ans < INT_MIN/10 || ans > INT_MAX/10){
    //             return 0;
    //         }
    //         ans *= 10;
    //         ans += tmp%(10);
    //         tmp /= 10;
    //         // cout<<ans<<"\n";
    //     }
    //     return x>0? ans: -ans;
    // }

    int reverse(int x){
        int ans = 0;
        while (x != 0)
        {
            if(ans < INT_MIN/10 || ans > INT_MAX/10){
                return 0;
            }

            ans = ans*10 + x%10;
            x /= 10;
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    Solution sol = Solution();
    cout<<sol.reverse(-12345);
    // cout<<sol.reverse(12341534236469);
    return 0;
}

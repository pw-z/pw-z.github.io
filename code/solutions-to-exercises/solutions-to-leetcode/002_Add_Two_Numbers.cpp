#include <iostream>

using std::cout;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        // cout<<l1->val<<"  "<<l2->val<<"\n";

        ListNode* result = new ListNode();
        ListNode* p_res = result;
        int temp1,temp2;
        int flag = 0;
        while ((l1 != nullptr || l2 != nullptr) || flag != 0)
        {
            temp1 = 0, temp2 = 0;
            if (l1 != nullptr){
                temp1 = l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr){
                temp2 = l2->val;
                l2 = l2->next;
            }
            int val = temp1 + temp2 + flag;
            flag = val >= 10 ? 1 : 0; 

            p_res->val = val >= 10 ? val-10:val;

            if ((l1 != nullptr || l2 != nullptr) || flag != 0){   
                p_res->next = new ListNode();
                p_res = p_res->next;
            }
        }
        // delete p_res;  // delete unnecessary node
        // p_res = nullptr;

        // while (result != nullptr)
        // {
        //     cout<<result->val<<" ";
        //     result = result->next;
        // }
        return result;
    }
};


void test(){
    ListNode* l1 = new ListNode(9);
    l1->next = new ListNode(8);
    ListNode* l2 = new ListNode(1);
    Solution* sol = new Solution();
    ListNode* res = sol->addTwoNumbers(l1, l2);
    while (res != nullptr)
    {
        cout<<res->val<<" ";
        res = res->next;
    }
}

int main(int argc, char const *argv[])
{
    
    test();
    return 0;
}



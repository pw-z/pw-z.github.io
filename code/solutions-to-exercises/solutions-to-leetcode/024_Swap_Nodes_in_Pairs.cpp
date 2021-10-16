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
class Solution {
    // 2021年10月16日08点46分
public:
    bool swapNodes(ListNode* pre, ListNode* cur){
        ListNode* next = cur->next;
        if(next != nullptr){
            pre->next = next;
            cur->next = next->next;
            next->next = cur;
            return true;
        }
        return false;
    }
    ListNode* swapPairs(ListNode* head) {
        ListNode* ans = new ListNode(-1);
        ans->next = head;

        ListNode* pre = ans;
        ListNode* first;
        first = head;
        while(first != nullptr && swapNodes(pre, first)){
            pre = first;
            first = first->next;
        }
        return ans->next;
    } 
    // 09点07分
};

/*
[2,3,6,7]
[3,2,7,6]

[]
[]

[1]
[1]

[1,2,3]
[2,1,3]
*/

/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：7.4 MB, 在所有 C++ 提交中击败了21.83% 的用户
*/
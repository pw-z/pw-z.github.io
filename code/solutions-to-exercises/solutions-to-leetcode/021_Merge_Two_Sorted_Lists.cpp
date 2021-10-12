struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution1 {
public:
    // 写完后分析：l1与l2的节点都是可以直接拿来用的，
    // 没必要每次新开辟内存生成一个新节点
    // Solution2是优化代码，也基本等同于官解方法二
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans_cur = new ListNode(0);
        ListNode* ans = ans_cur;
        while(l1 != nullptr && l2 != nullptr){
            if(l1->val <= l2->val){
                ListNode* temp = new ListNode(l1->val);
                ans_cur->next = temp;
                l1 = l1->next;
            }else{
                ListNode* temp = new ListNode(l2->val);
                ans_cur->next = temp;
                l2 = l2->next;
            }
            ans_cur = ans_cur->next;
        }

        while(l1 != nullptr){
            ans_cur->next = l1;
            ans_cur = ans_cur->next;
            l1 = l1->next;
        }
        while(l2 != nullptr){
            ans_cur->next = l2;
            ans_cur = ans_cur->next;
            l2 = l2->next;
        }

        return ans->next;
    }
};


class Solution2 {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* ans_cur = new ListNode(-1);
        ListNode* ans = ans_cur;

        while(l1 != nullptr && l2 != nullptr){
            if(l1->val < l2->val){
                ans_cur->next = l1;
                l1 = l1->next;
            }else{
                ans_cur->next = l2;
                l2 = l2->next;
            }
            ans_cur = ans_cur->next;
        }
        // while(l1 != nullptr){
        //     ans_cur->next = l1;
        //     ans_cur = ans_cur->next;
        //     l1 = l1->next;
        // }
        // while(l2 != nullptr){
        //     ans_cur->next = l2;
        //     ans_cur = ans_cur->next;
        //     l2 = l2->next;
        // }
        ans_cur->next = l1 == nullptr? l2 : l1;
        return ans->next;
    }
};
/*
执行用时：8 ms, 在所有 C++ 提交中击败了65.11% 的用户
内存消耗：14.5 MB, 在所有 C++ 提交中击败了31.41% 的用户
*/
#include<algorithm>
#include<queue>

using std::max;
using std::queue;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*
递归解法，不断想左右两颗子树递归，直到叶子节点后自底向上返回树的高度
*/
class Solution_DFS {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right))+1;
    }
};
/*
执行用时：4 ms, 在所有 C++ 提交中击败了95.13% 的用户
内存消耗：18.4 MB, 在所有 C++ 提交中击败了76.16% 的用户
*/


/*
广度优先搜索，每次遍历一整层，每向下一层则最大高度+1
*/
class Solution_BFS {
public:
    int maxDepth(TreeNode* root) {
        queue<TreeNode*> que;
        if(root == nullptr) return 0;
        que.push(root);
        int high = 1;
        int count=1, temp_count=0;
        while(que.size() > 0 && count>0){
            TreeNode* t = que.front();
            que.pop();
            --count;
            if(t->left != nullptr) {
                que.push(t->left);
                ++temp_count;
            }
            if(t->right != nullptr){
                que.push(t->right);
                ++temp_count;
            }
            if(count == 0 && temp_count > 0){
                count = temp_count;
                temp_count = 0;
                ++high;
            }
        }
        return high;
    }
};
/*
执行用时：4 ms, 在所有 C++ 提交中击败了95.13% 的用户
内存消耗：18.5 MB, 在所有 C++ 提交中击败了17.27% 的用户
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    vector<TreeNode*> result;
    unordered_map<string, int> count;
    int tag = 0;
    string dfs(TreeNode* t){
        ++tag;
        if(t != nullptr){
            string s = to_string(t->val) + "." + dfs(t->left) +"."+ dfs(t->right);
            if(count.count(s) > 0){
                if(count[s] == 1){
                    result.push_back(t);
                }
                ++count[s];
            }else{
                count[s] = 1;
            }
            return s;
        }else{
            return "#";
        }
    }
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        dfs(root);
        return result;
    }
};
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
    public:
        int diameterOfBinaryTree(TreeNode* root) {
            int d=0;
            CalcHeightNode(root, d);
            return d;
            
        }
         int CalcHeightNode(TreeNode* node, int& d){
            if(!node) return 0;
            int leftht =CalcHeightNode(node->left, d);
            int rightht =CalcHeightNode(node->right, d);
            
            d = max(d,(leftht+rightht));
            
            return 1 + max(leftht, rightht);
        }
        
    };
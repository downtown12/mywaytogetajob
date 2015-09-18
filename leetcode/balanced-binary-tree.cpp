#include<iostream>
using namespace std;
//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        int ldepth = 0;
        int rdepth = 0;
        
        //extreme condition
        if (root == NULL)
            return true;
        
        int depth_diff = calDepth(root->left) - calDepth(root->right);
        if (depth_diff<0)
            depth_diff = -depth_diff;
        cout<<depth_diff<<endl;    
        if(depth_diff <=1)
            return true;
        else
            cout<<"false"<<endl;
            return false;
    }
    
    int calDepth(TreeNode * root){
        int ldepth=0, rdepth=0;
        if (root == NULL){
            return 0;
        }
        ldepth = 1+ calDepth(root->left);
        rdepth = 1+ calDepth(root->right);
    
        return ldepth>rdepth?ldepth:rdepth;
    }
};

int main()
{
    TreeNode * root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(2);
    root->left->left = new TreeNode(3);
    root->left->left->left = new TreeNode(4);
    
    Solution * s = new Solution();
    cout<<s->calDepth(root->left)<<endl;
    cout<<s->calDepth(root->right)<<endl;
    
    cout<<s->isBalanced(root)<<endl;
    return 0;
}

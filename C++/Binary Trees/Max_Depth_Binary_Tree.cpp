// Maximum depth in a binary tree
// Author: Pavan Kumar Paluri
// Leetcode Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    int maxDepth(TreeNode* root) {
        if(root==nullptr)
            return 0;
        queue<TreeNode*> que;
        vector<vector<int>> node_values;
        // Initially Push the root value 
        que.push(root);
        
        while(!que.empty())
        {
            vector<int>v1;
            int var = que.size();
            for(int i=0; i<var; i++)
            {
                TreeNode* current = que.front();
                // now pop the "oldest" element 
                v1.push_back(current->val);
                que.pop();
                if(current->left!=nullptr)
                    que.push(current->left);
                if(current->right!=nullptr)
                    que.push(current->right);  
                    
            }
            node_values.push_back(v1);
            v1.clear();
            
        }
        /*
        for (int i = 0; i < node_values.size(); i++)
{
    for (int j = 0; j < node_values[i].size(); j++)
    {
        cout << node_values[i][j];
    }
            cout << " ";
}
*/
        return node_values.size();
    }
};

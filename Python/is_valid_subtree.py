# Function to check if a given subtree is a valid subtree of a given larger tree
# Author: Pavan Kumar Paluri
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return True 
        if s is None:
            return False 
        
        # Check individual nodes
        if self.is_valid(s, t):
            return True 
        
        # Explore each node one by one 
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def is_valid(self, r1, r2):
        if r2 is None and r1 is None:
            return True 
        if r1 is None or r2 is None: # either of them are None 
            return False
        '''
        if r1.val == r2.val:
            return True
            '''
        return (r1.val==r2.val)and self.is_valid(r1.left, r2.left) and self.is_valid(r1.right, r2.right)
    

# Author: Pavan Kumar Paluri
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        elif root is not None:
            if root.val == val:
                return root
            elif root.val > val:
                # If val to be searched is less than root's value 
                if root.left is not None:
                    return self.searchBST(root.left, val)
            elif root.val < val:
                # If val to be searched is greater than root's value
                if root.right is not None:
                    return self.searchBST(root.right, val)
  

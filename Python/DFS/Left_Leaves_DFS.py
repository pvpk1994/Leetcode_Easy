# Depth-First Search Sum of all left-leaves in a BST
# Author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # using Pre-order traversal - DFS
        if root is None:
            return 0
        left_values= []
        # using recursion
        current = root
        summ = 0
        def helper(current:TreeNode, summ:int, marker:bool):
            if current is not None:
                # current 
                if current.left is None and current.right is None and marker:
                    left_values.append(current.val)
                if current.left is not None:
                    marker = True
                    helper(current.left, summ, marker)
                if current.right is not None:
                    marker = False
                    helper(current.right, summ, marker)
            return summ
        helper(current, 0, False)
        return sum(left_values)

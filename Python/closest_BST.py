# Find the closest value to a given target in a Binary Search Tree
# Author: Pavan Kumar Paluri
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def __init__(self):
        self.base_val = 0
    def closestValue(self, root: TreeNode, target: float) -> int:
        # target = math.ceil(target)
        min_val = math.inf
        def helper(root, target, min_val):
            if root is not None:
                diff = abs(target-root.val)
                if diff < min_val:
                    min_val = diff
                    self.base_val = root.val
                        
                if root.left is not None:
                    helper(root.left, target, min_val)
                if root.right is not None:
                    helper(root.right, target, min_val)
        helper(root, target, min_val)
        return self.base_val
        

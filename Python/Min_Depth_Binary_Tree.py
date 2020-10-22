# Calculate the minimum depth of binary tree
# Using stack and recursion
# Author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        height = []
        stack = []
        def helper(root):
            if root is None:
                return 
            stack.append(root)
            if root.left is None and root.right is None:
                height.append(len(stack))
            helper(root.left)
            helper(root.right)
            stack.pop()
        helper(root)
        return min(height)

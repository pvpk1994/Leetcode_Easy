# Find the sum of all left-leaves in a BST
# Author: Pavan Kumar Paluri
# LeetCode Question: https://leetcode.com/problems/sum-of-left-leaves/


from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Breadth first search 
        if root is None:
            return 0
        que = deque([root,])
        left_nodes = []
        left_val = []
        while que:
            current = que.popleft()
            if current.left is None and current.right is None and current in left_nodes:
                left_val.append(current.val)
            if current.left is not None:
                que.append(current.left)
                left_nodes.append(current.left)
            if current.right is not None:
                que.append(current.right)
        return sum(left_val)

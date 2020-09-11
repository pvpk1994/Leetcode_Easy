# Tilt Binary tree around the root Node
# Author: Pavan Kumar Paluri
# LeetCode Question: https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.final_res = 0
        
    def findTilt(self, root: TreeNode) -> int:
        def helper(current:TreeNode):
            if current is None:
                return 0
            left_val = helper(current.left)
            right_val = helper(current.right)
            self.final_res += abs(left_val-right_val)
            return left_val+right_val+current.val
        helper(root)
        return self.final_res

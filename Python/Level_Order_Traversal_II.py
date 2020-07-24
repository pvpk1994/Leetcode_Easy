from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        output = []
        # Init a que with its root as top node 
        que = deque([root, ])
        level  =0
        while que and root:
            length_q = len(que)
            output.append([]) # init an empty list
            # current = que.popleft() # current is the root node now
            for _ in range(length_q):
                current = que.popleft()
                output[level].append(current.val)
                if current.left is not None:
                    que.append(current.left)
                    #output[level].append(current.left.val)
                if current.right is not None:
                    que.append(current.right)
                    #output[level].append(current.right.val)
            level += 1
        return output[::-1]
 

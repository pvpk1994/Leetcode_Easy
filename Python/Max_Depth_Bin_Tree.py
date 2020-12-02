# Leetcode Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Author: Pavan Kumar Paluri

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###### -- Depth First Search ----- #####
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # maximum depth of binary tree 
        # Using recursion and maintaining a stack
        if root is None:
            return 0
        node_stack = []
        len_stack =[]
        max_depth = -math.inf
        # Preorder (root, left, right)
        def preorder(root:TreeNode, max_depth):
            if root is None:
                return 
            node_stack.append(root)
            if root.left is None and root.right is None:
                # Leaf node reached 
                len_stack.append(len(node_stack))
                
            preorder(root.left, max_depth)
            preorder(root.right, max_depth)
            node_stack.pop()
        preorder(root, max_depth)
        return max(len_stack)
    
###### ----- Breadth First Search ---- ####
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        que = deque([root, ])
        nodes=[]
        level =0
        while que:
            nodes.append([])
            for i in range(0, len(que)):
                root = que.popleft()
                nodes[level].append(root.val)
                if root.left is not None:
                    que.append(root.left)
                if root.right is not None:
                    que.append(root.right)
            level+=1 
        print(nodes)
        return len(nodes)

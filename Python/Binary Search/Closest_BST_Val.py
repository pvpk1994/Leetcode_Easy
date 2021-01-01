# Given a target return the closest value to the target in a BST
# The most desirable solution should consume Constant Space O(1) and Should run in O(H) where H is the maximum height of the BST (Worst Case)
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

# Time Complexity of the approach:: O(H) since atmost Height of the tree is explored 
def findClosestValueInBst(tree, target):
    # Write your code here.
    # using binary search
	closest_node = tree.value 
	while tree:
		closest_node = min(closest_node, tree.value, key=lambda y: abs(target-y))
		tree = tree.left if target < tree.value else tree.right
	return closest_node


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

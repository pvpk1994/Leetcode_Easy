# Depth First Search graph traversal 
# Author: Pavan Kumar paluri
# Time Complexity: O(V+E) and Space Complexity: O(V) 
# Algo Expert Question: https://www.algoexpert.io/questions/Depth-first%20Search

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        # load root node
		array.append(self.name)
		# self.children now has [B, C, D] for sample input
		for child in self.children:
			child.depthFirstSearch(array)
		return array

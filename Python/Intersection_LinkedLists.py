# Find the common intersection node in LinkedLists A and B
# Author: Pavan Kumar Paluri

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution:
	# Approach-1: Time Complexity: O(m+n) Space: O(1)
	def getIntersectionNode(self, headA: Node, headB: Node) -> Node:
		if headA == None or headB == None:
			return None
		# Init head ptrs
		ptr_A = headA
		ptr_B = headB

		# Iterate 
		while ptr_A != ptr_B:
			if ptr_A == None:
				# time to point ptr_A to headB
				ptr_A = headB
			else:
				ptr_A = ptr_A.next

			# same for B
			if ptr_B == None:
				# time to change to A
				ptr_B = headA
			else:
				ptr_B = ptr_B.next
		# if here: ptr_A == ptr_B
		return ptr_A

	# Approach-2: Time Complexity: O(m+n) Space: O(m) or O(n)
	def getIntersectionNode2(self, headerA:Node, headerB:Node)->Node:
		# print("HeaderA: " + str(headerA.val))
		# print("HeaderB: " + str(headerB.val))
		set_A = set()
		ptrA = headerA
		ptrB = headerB
		# print(ptrA.next.val)
		# print(ptrB.next.val)
		while ptrA is not None:
			set_A.add(ptrA)
			ptrA = ptrA.next
		while ptrB is not None:
			if ptrB in set_A:
				return ptrB
			ptrB = ptrB.next
		# If none found: return None
		return None



if __name__ == "__main__":
	# Create LinkedList 1:
	rootA = Node(1)
	rootA1=rootA.next = Node(9)
	rootA2=rootA1.next = Node(1)
	rootA3=rootA2.next = Node(2)
	rootA4=rootA3.next = Node(4)
	
	# Create LinkedList 2:
	rootB = Node(5)
	rootB1= rootB.next = Node(3)
	rootB2 = rootB1.next = Node(3)
	rootB3 = rootB2.next = rootA1
	rootB4 = rootB3.next = rootA2 

	sol = Solution()
	print((sol.getIntersectionNode(rootA, rootB)).val)
	print((sol.getIntersectionNode2(rootA, rootB)).val)

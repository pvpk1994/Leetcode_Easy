# Auhtor: Pavan Kumar Paluri
# Delete a node given its value
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # delete the node with a given int val
        def_node = ListNode(-1)
        #link with the head
        def_node.next = head
        
        current = head
        prev = def_node
        while current is not None:
            if current.val==val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return def_node.next

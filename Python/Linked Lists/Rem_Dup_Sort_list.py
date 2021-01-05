# Remove Duplicates from sorted linkedlist
# Author: Pavan Kumar Paluri

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Time Complexity: O(N) and Space O(1)
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head 
        
        '''
        # Time Complexity: O(N) and Space Complexity: O(N)
        h_set = set()
        prev_node = ListNode(-1)
        current = prev_node
        while head is not None:
            if head.val not in h_set:
                current.next = head
                current = current.next
                print(current)
                h_set.add(head.val)
            head = head.next
        current.next = None
        print(h_set)
        return prev_node.next
        '''
        

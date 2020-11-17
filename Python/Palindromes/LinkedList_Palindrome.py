# LinkedList Palindrome
# Time Complexity: O(N) and Space Complexity: O(N)
# LeetCode Question: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(n) and Space Complexity: O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1=[]
        # iterate to the end of the linkedlist stroing each node's val
        while head is not None:
            l1.append(head.val)
            head = head.next
        if l1==l1[::-1]:
            return True
        else:
            return False 

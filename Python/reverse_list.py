# Swap Nodes in a given Linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  # Returns a head node after swapping every element in the linkedlist
  def swap_pairs(self, head:Node)->Node:
    if head is None or head.next is None:
      return head  # or return None
    first_node = head
    second_node = head.next 

    first_node.next = self.swap_pairs(second_node.next) # using recursion
    second_node.next = first_node
    return second_node

  # Reverse a Linked list - Iterative Approach
  def reverse_iterative(self, head:Node)->Node:
    previous_node = None
    current_node = head
    while(current_node):
      temp_node = current_node.next
      current_node.next = previous_node
      previous_node = current_node
      current_node = temp_node
    return previous_node
    
  # Reverse a Linked List - Recursive Approach
  def reverse_recursive(self, head:Node)->Node:
    if head is None or head.next is None:
      return head
    p = self.reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return p

  def print_nodes(self, head: Node):
    while head is not None:
      print(head.val, "-> ", end="")
      head = head.next
    print("None")

if __name__=="__main__":
  root = Node(12)
  root.next = Node(34)
  root.next.next = Node(53)
  root.next.next.next = Node(14)
  linkedlst = LinkedList()
  '''
  print("*** Before Swap ***")
  linkedlst.print_nodes(root)
  root_node = linkedlst.swap_pairs(root)
  print("\n")
  print("*** After Swap ***")
  linkedlst.print_nodes(root_node)
  
  print("*** Reversal of Linked List - Iterative Approach ****")
  rn =linkedlst.reverse_iterative(root)
  linkedlst.print_nodes(rn)
  '''
  print("**** Reversal Linked List - Recursion ****")
  rn = linkedlst.reverse_recursive(root)
  linkedlst.print_nodes(rn)


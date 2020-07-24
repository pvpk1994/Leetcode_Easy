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
  print("*** Before Swap ***")
  linkedlst.print_nodes(root)
  root_node = linkedlst.swap_pairs(root)
  print("\n")
  print("*** After Swap ***")
  linkedlst.print_nodes(root_node)

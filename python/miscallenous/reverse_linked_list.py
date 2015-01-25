class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

  def __str__(self):
    result = ""
    node = self
    while node:
      result += "{0} -> ".format(node.data)
      node = node.next
    return result

def reverse_list_nondestructive(head):
  current_node = head
  next_node = head.next
  head.next = None
  while next_node:
      temp_node = next_node.next
      next_node.next = current_node

      new_head = Node()
      head = head.next
  return new_head


n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(40)

print(n)
print(reverse_list_nondestructive(n))

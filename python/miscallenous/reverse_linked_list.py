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

#Iterative
def reverse_list_iterative(head):
  last = None
  current = head

  while(current is not None):
    next_node = current.next
    current.next = last
    last = current
    current = next_node

  return last

def reverse_list_recursive(node,last=None):
  if node is None:
    return last
  next_node = node.next
  node.next = last
  return reverse_list_recursive(next_node, node)


n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(40)

print(n)
print reverse_list_recursive(n)
# print(reverse_list_nondestructive(n))

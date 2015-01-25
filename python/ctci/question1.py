from node import Node;

def remove_duplicates(node):
  counts = {}
  # counts[node.data] = True
  while node:
    if node.next.data in counts:
      node.next = node.next.next
    else:
      print node
      counts[node.data] = True
    if node.next == None:
      break
    node = node.next


n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(20)
n.next.next.next.next = Node(40)
n.next.next.next.next.next = Node(30)
remove_duplicates(n)
print (n)

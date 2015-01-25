class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    result = ""
    node = self
    while node is not None:
      result += "({0})->".format(node.data)
      node = node.next
    return result

  def __len__(self):
    result = 0
    node = self
    while node is not None:
      result += 1
      node = node.next
    return result

def kth_to_last(node, k):
  length = len(node)
  if k > length:
    return -1

  visited = length
  while node:
    if visited == k:
      return node.data
    visited -= 1
    node = node.next

def recursive_kth_to_last(head, k):
  p1 = head
  p2 = head

  for i in range(k - 1):
    if p2 is None: return None
    p2 = p2.next

  if p2 is None: return None

  while p2.next is not None:
    p1 = p1.next
    p2 = p2.next
  return p1.data


n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(40)
n.next.next.next.next = Node(50)

print kth_to_last(n, 1)
print kth_to_last(n, 2)
print kth_to_last(n, 3)

print recursive_kth_to_last(n, 1)
print recursive_kth_to_last(n, 2)
print recursive_kth_to_last(n, 3)

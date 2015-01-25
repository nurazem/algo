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

def remove_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


n = Node(10)
n.next = Node(20)
n.next.next = Node(30)
n.next.next.next = Node(40)
n.next.next.next.next = Node(50)

print n
remove_middle_node(n.next.next)
print n



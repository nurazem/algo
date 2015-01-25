class Queue:
  def __init__(self):
    self.data = []

  def __len__(self):
    return len(self.data)

  def push(self, item):
    self.data.extend([item])

  def pop(self):
    popped_item = self.data[0]
    self.data = self.data[1:]
    return popped_item

  def peek(self):
    return self.data[0]

  def __str__(self):
    return str(self.data)

class Node:
  def __init__(self, data):
    self.data = data
    self.children = []

  def __str__(self):
    return "( " + str(self.data) + " ( " + str(self.children) + "))"

class LinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

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

  def __str__(self):
    result = ""
    node = self
    while node is not None:
      result += "({0})->".format(node.data)
      node = node.next
    return result

def linked_list_from_array(arr):
  if len(arr) > 0:
    head = LinkedListNode(arr[0])
    pointer = head
    for i in range(1, len(arr)):
      pointer.next = LinkedListNode(arr[i])
      pointer = pointer.next
    return head
  else:
    return None

def bst(root):
  queue = Queue()
  queue.push(root)
  result = [LinkedListNode(root.data)]

  while len(queue) > 1:
    node = queue.pop()
    result.append(linked_list_from_array(node.children))
    queue.push(node.children)

  return result

def bst_print(root):
  queue = Queue()
  queue.push(root)
  print str(root.data)

  while len(queue) > 0:
    print queue
    node = queue.pop()
    queue.push(node.children)

n = Node(10)
m = Node(20)
l = Node(60)
m.children = [Node(30), Node(40), Node(50), Node(60)]
l.children = [Node(30), Node(40), Node(50), Node(60)]
n.children = [m, n]

bst_print(n)
# print bst(n)
# print map(str, bst(n))

# n = LinkedListNode(10)
# print n
# print linked_list_from_array([1, 2, 3, 4, 5, 6, 7])


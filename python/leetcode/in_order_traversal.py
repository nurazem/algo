class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def inorder_array(node, partial=None):
  if partial==None:
    partial = []
  if node == None:
    return None
  if node.left != None:
    inorder_array(node.left, partial)

  partial.append(node.val)

  if node.right != None:
    inorder_array(node.right, partial)
  return partial

def postorder_array(node, partial=None):
  if partial==None:
    partial = []
  if node == None:
    return None
  if node.left != None:
    inorder_array(node.left, partial)
  if node.right != None:
    inorder_array(node.right, partial)
  partial.append(node.val)
  return partial

def dfs(node, value):
  if node.val == value:
    return True
  print node.val
  if node.left != None:
    dfs(node.left, value)
  if node.right != None:
    dfs(node.right, value)
  return False

n = Node(10)
n.left = Node(9)
n.right = Node(11)
n.left.left = Node(7)
n.left.right = Node(8)
n.left.left.left = Node(1)
n.left.left.right = Node(5)
n.right.right = Node(12)

print inorder_array(n)
print postorder_array(n)
print dfs(n, 11)

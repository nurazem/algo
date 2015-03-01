# This solution is incorrect
def sum_of_nodes(root):
  d = tree_depth(root)
  p = d
  result = 0
  current_nodes = [root]
  while current_nodes:
    print current_nodes
    next_nodes = []
    for cn in current_nodes:
      result += cn.val * (10 ** (p - 1)) * (d + 1)
      if cn.left != None:
        next_nodes.append(cn.left)
      if cn.right != None:
        next_nodes.append(cn.right)
    d /= 2
    p -= 1
    current_nodes = next_nodes
  return result

def tree_depth(root):
  if root == None:
    return 0
  if root.left == None and root.left == None:
    return 1
  elif root.left != None and root.right == None:
    return tree_depth(root.right) + 1
  elif root.right != None and root.left == None:
    return tree_depth(root.left) + 1
  else:
    return max(tree_depth(root.left), tree_depth(root.right)) + 1

def sum_root_to_leaves(root, result=None):
  if result == None: result = 0
  if root == None:
    return 0

  result = result * 10 + root.val
  if root.left == None and root.right == None:
    return result

  return sum_root_to_leaves(root.left, result) + sum_root_to_leaves(root.right, result)


class TreeNode(object):
  """docstring for TreeNode"""
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

n = TreeNode(6)
n.left = TreeNode(3)
n.right = TreeNode(5)
n.left.left = TreeNode(3)
n.left.right = TreeNode(5)
n.left.right.left = TreeNode(7)
n.left.right.right = TreeNode(4)
n.right.right = TreeNode(4)

print sum_root_to_leaves(n)

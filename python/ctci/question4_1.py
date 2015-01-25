import random

class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def __str__(self):
    return "( " + str(self.data) + " ( " + str(self.left) + " | " + str(self.right) + "))"

  @staticmethod
  def treeHeight(root):
    if root is None: return 0
    return max(BinaryTree.treeHeight(root.left), BinaryTree.treeHeight(root.right)) + 1

  # def is_balanced(btree):
  #   return 1
  @staticmethod
  def unbalanced_tree(depth):
    bt1 = BinaryTree(1)
    for i in range(2, depth):
      bt2 = BinaryTree(i)
      bt2.left = bt1
      bt1 = bt2
    return bt1

  @staticmethod
  def is_balanced(btree):
    if btree is None: return True
    height_diff = abs(BinaryTree.treeHeight(btree.left) - BinaryTree.treeHeight(btree.right))
    if height_diff > 1:
      return False
    else:
      return BinaryTree.is_balanced(btree.left) and BinaryTree.is_balanced(btree.right)

  @staticmethod
  def balanced_tree(depth):
    if depth>0:
        tree = BinaryTree(random.randint(0, 100))
        tree.left = BinaryTree.balanced_tree(depth-1)
        tree.right = BinaryTree.balanced_tree(depth-1)
        return tree
    else:
        return None

print BinaryTree.is_balanced(BinaryTree.unbalanced_tree(100))
print BinaryTree.is_balanced(BinaryTree.balanced_tree(3))
print BinaryTree.balanced_tree(3)

class BinaryTree:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def __str__(self):
    return "( " + str(self.data) + " ( " + str(self.left) + " | " + str(self.right) + "))"


def is_bst(btree, lower_bound = -100, upper_bound = 100):
  if btree is None: return True

  return lower_bound < btree.data < upper_bound and \
    is_bst(btree.left, lower_bound, btree.data) and \
    is_bst(btree.right, btree.data, upper_bound)


btree = BinaryTree(10, BinaryTree(9), BinaryTree(12))
# btree.left.left = BinaryTree(7, BinaryTree(6), BinaryTree(8))
# btree.right.right = BinaryTree(14, BinaryTree(12), BinaryTree(13))

print btree
print is_bst(btree)

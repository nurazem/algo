class BinarySearchTree:
  def __init__(self, content, left = None, right = None):
    self.content = content
    self.left = left
    self.right = right

  def traverse(self):
    thislevel = [self]
    while thislevel:
      nextlevel = list()
      for n in thislevel:
        print n.content,
        if n.left: nextlevel.append(n.left)
        if n.right: nextlevel.append(n.right)
      print
      thislevel = nextlevel

def int_array_to_bst(array):
  if len(array) == 0:
    return None
  elif len(array) == 1:
    return BinarySearchTree(array[0])
  else:
    cutoff = len(array) / 2
    bst = BinarySearchTree(array[cutoff])
    bst.left = int_array_to_bst(array[:cutoff])
    bst.right = int_array_to_bst(array[cutoff + 1:])
    return bst

print int_array_to_bst([1, 2, 3, 4, 5, 6, 7, 8]).traverse()

def unival_tree(root):

  if root.left == None and root.right == None:
    return True
  elif root.left == None and root.right != None:
    return root.right.val == root.val and unival_tree(root.right)
  elif root.right == None and root.left != None:
    return root.left.val == root.val and unival_tree(root.right)
  else:
    return root.left.val == root.val and root.right.val == root.val and unival_tree(root.right) and unival_tree(root.right)


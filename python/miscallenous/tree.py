#binary tree python
class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        #-1 means the depth has not been calculated yet.
        self.depth = -1

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))"

bt = BinaryTree(10)
bt.left = BinaryTree(20)
bt.left.left = BinaryTree(30)
bt.right = BinaryTree(20)
bt.right.right = BinaryTree(30)

print bt

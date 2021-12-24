# write a function to determine the number of nodes in a binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def countNodes(node):
    if node is None:
        return 0
    return 1 + countNodes(node.left) + countNodes(node.right)

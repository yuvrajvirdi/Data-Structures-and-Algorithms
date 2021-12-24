# Write a function to calculate the height / depth of a binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def treeHeight(node):
    if node is None:
        return 0
    # returns 1 (base of the tree) added to the length of
    # either the left or right sub tree, depending on which one is longer
    return 1 + max(treeHeight(node.left), treeHeight(node.right))

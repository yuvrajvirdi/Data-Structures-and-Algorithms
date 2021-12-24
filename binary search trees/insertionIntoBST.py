# write a function to insert a new node into a Binary Search Tree

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    # ending condition, if node is none, then create a new BSTNode, which then returns the node.
    if node is None:
        node = BSTNode(key, value)
    # if key is less than current node's key, insert it into the left subtree
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    # if key is greater than current node's key, insert it inot the right subtree
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
        
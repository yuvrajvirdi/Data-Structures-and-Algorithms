# find the value associated with a given key in a BST

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def find(node, key):
    # if it DNE, return none
    if node is None:
        return None
    # ending statement, returns node pointer if found
    if key == node.key:
        return node
    # if key is less than current node's key, recurisevely search left subtree
    if key < node.key:
        return find(node.left, key)
    # if key is greater than current node's key, recursively search right subtree
    if key > node.key:
        return find(node.right, key)
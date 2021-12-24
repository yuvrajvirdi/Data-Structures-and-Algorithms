# Write a function to retrieve all the key-value pairs stored in a BST in the sorted order or keys

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def listAll(node):
    if node is None:
        return []
    # gives list of key values pair in the left subtree, current node, and right subtree in that order.
    return listAll(node.left) + [(node.key, node.value)] + listAll(node.right)
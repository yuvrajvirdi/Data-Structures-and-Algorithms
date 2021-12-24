class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def traverseInOrder(node):
    if node is None:
        return []
    return (traverseInOrder(node.left) + 
            [node.key] + 
            traverseInOrder(node.right))
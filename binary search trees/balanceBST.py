# Write a function to balance an unbalanced binary search tree

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# creates a balanced BST from a sorted arrat of key value pairs
def createBalancedBST(data, low = 0, high = None, parent = None):
    if high is None:
        high = len(data) - 1
    if low > high:
        return None
    
    mid = (low + high) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = createBalancedBST(data, low, mid-1, root)
    root.right = createBalancedBST(data, mid+1, high, root)

    return root
# gets a list of key value pairs
def listAll(node):
    if node is None:
        return []
    # gives list of key values pair in the left subtree, current node, and right subtree in that order.
    return listAll(node.left) + [(node.key, node.value)] + listAll(node.right)

def balanceBST(node):
    return createBalancedBST(listAll(node))

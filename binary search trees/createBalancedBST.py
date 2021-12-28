'''
Write a function to create a balanced BST from a sorted 
list/array of key-value pairs
'''

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key 
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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

# convert the following tuple to a binary tree
treeTuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def tupleToBinaryTree(data):
    # checks if data is a tuple type and if it has a length of three
    if isinstance(data,tuple) and len(data) == 3:
        # creates a center node using the second element in tuple
        node = TreeNode(data[1])
        # sets first element of tuple as the left subtree of node
        node.left = tupleToBinaryTree(data[0])
        # sets last element of tuple as the right subtree of node
        node.right = tupleToBinaryTree(data[2])
    # if node is none
    elif data is None:
        node = None
    # if node is a number
    else:
        node = TreeNode(data)
    return node
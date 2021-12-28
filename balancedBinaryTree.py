# write a function to determine if a binary tree is balanced

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def isBalanced(node):
    if node is None:
        return True, 0
    balancedLeft, heightLeft =  isBalanced(node.left)
    balancedRight, heightRight = isBalanced(node.right)
    balanced = balancedLeft and balancedRight and abs(heightLeft - heightRight) <= 1
    height = 1 + max(heightLeft, heightRight)
    return balanced, height
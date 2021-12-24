# write a function to see if a binary tree is a binary search tree, 
# and find the max and min keys if they exist

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def removeNone(nums):
    for x in nums:
        if x is not None:
            return x

def isBST(node):
    if node is None:
        return True, None, None

    is_BST_Left, minLeft, maxLeft =  isBST(node.left)
    is_BST_Right, minRight, maxRight = isBST(node.right)

    is_BST_Node =  (is_BST_Left and is_BST_Right and
                    (maxLeft is None or node.key > maxLeft) and
                    (minRight is None or node.key < minRight))

    minKey = min(removeNone([minLeft, node.key, minRight]))
    maxKey = max(removeNone([maxLeft, node.key, maxRight])) 

    return is_BST_Node, minKey, maxKey


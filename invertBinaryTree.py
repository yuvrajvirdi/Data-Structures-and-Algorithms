# binary tree

class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

# inverting binary tree

class Solution:
    def invertBinaryTree(self, root):
        stack = [root] # root as array
        while stack:
            node = stack.pop() # assigns node value as stack popped element
            if node:
                node.left, node.right = node.right, node.left # swapping nodes
                stack += [node.left, node.right]
        return root

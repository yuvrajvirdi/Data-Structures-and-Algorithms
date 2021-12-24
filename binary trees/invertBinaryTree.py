# binary tree

class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

# inverting binary tree

class Solution:
    def invertBinaryTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left # swapping nodes
                stack+=[node.left, node.right]
        return root

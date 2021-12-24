class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None





node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

tree = node0 

tree.key # gives value of 3
tree.left.key # gives value of 4
tree.right.key # gives value of 5
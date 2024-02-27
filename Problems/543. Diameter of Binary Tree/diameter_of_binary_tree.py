class Solution:
    def __init__(self):
        self.diameter = 0 # max diamter found

    # calculate max depth of the left and right side of the given node
    # determine the diameter of the given node and check if its the maximum
    def depth(self, node):
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right) # return depth ( plus 1 to account for root node )
    
    def diameterOfBinaryTree(self, root):
        self.depth(root)
        return self.diameter
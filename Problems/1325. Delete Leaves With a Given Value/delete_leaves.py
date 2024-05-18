class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root, target):
        # if no nodes left return empty object
        if not root:
            return None
        # recursively traverse the left and right child nodes and remove target leaves
        root.right = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # if the node has no child nodes ( it is a leaf node )
        # and its value is target return an empty object
        if not root.left and not root.right and root.val == target:
            return None
        
        # return the binary tree with the target leaf nodes removed
        return root
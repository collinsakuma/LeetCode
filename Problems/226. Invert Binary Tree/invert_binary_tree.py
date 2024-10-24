class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def invertTree(self, root):
        # if Binary Tree is empty return the empty tree
        if not root:
            return root
        
        # create a new binary tree to build in the inverted tree
        new_root = TreeNode(root.val)

        # depth first search recursive fucntion
        def dfs(root, new_root):
            # if there is a left child node
            if root.left:
                # create a right node in the new tree
                new_root.right = TreeNode(root.left.val)
                # traverse the original root left and the new tree right
                dfs(root.left, new_root.right)
            # if there is a right child node
            if root.right:
                # create a left node in the new tree
                new_root.left = TreeNode(root.right.val)
                # traverse the original root right and the new tree left
                dfs(root.right, new_root.left)

        dfs(root.new_root) # invert the tree

        return new_root # return the inverted tree
    
    def invertTreeTwo(self, root):
        # if binary tree is empty return an the empty tree
        if not root:
            return root
        
        # recursively invert the tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # swap the left and right values of the nodes
        root.left, root.right = root.right, root.left

        return root # return the inverted binary tree
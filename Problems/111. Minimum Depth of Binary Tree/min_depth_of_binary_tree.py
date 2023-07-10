class Solution:
    def minDepth(self, root):
        if not root: # check if the binary tree exist if not return 0
            return 0
        
        # find the depth of both sides of the binary tree
        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)

        if root.left and root.right: # if there is a left and right node of the binary tree
            return min(left, right) + 1 # return the minimum depth of the binary tree. Add one to account for the top layer of the tree.

        return max(left, right) + 1 # if the binary tree only consist of one side return the max value for that one side
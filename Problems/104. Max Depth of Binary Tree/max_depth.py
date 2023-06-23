class Solution:
    def maxDepth(self, root):
        if not root: # if not a binary tree return 0 as there is no possible depth to check
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # check both sides of the binary tree for their depth and return the value that is greater plus 1( to account for root )
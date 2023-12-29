class Solution:
    def isBalanced(self, root):
        return self.Height(root) >= 0

    # helper function to determine height of each side of the binary tree
    def Height(self, root):
        if root is None:
            return 0
        left_height, right_height = self.Height(root.left), self.Height(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
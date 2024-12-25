class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestvalues(self, root):
        # if no nodes in root return an empty list
        if not root: return []

        largest_values = []

        def traverse_tree(node, level):
            # if a new row of the binary tree is reached add a new largest value for that row
            if len(largest_values) < level + 1:
                largest_values.append(node.val)

            # check if a new largest value for the row has been found
            largest_values[level] = max(largest_values[level], node.val)

            # traverse the children nodes of root increment level
            if node.left: traverse_tree(node.left, level + 1)
            if node.right: traverse_tree(node.right, level + 1)

        # recursively traverse the binary tree for the largest values of rows
        traverse_tree(root, 0)

        # return the largest values of each row
        return largest_values
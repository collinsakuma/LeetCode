class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root, k):
        level_sum = [] # array to hold the sum of each level in the tree

        # recursively traverse the tree
        def traverse(root, level):
            # add levels to the levels array if necesssary
            if level == len(level_sum):
                level_sum.append(0)

            # add the nodes value to its level
            level_sum[level] += root.val

            # check for left and right child nodes and recurvely add then to levels
            if root.left:
                traverse(root.left, level + 1)
            if root.right:
                traverse(root.right, level + 1)
        
        # traverse the root summing up each level
        traverse(root, 0)

        # if there are less than k levels return -1
        if len(level_sum) < k:
            return -1
        # return the kth largest level sum
        else:
            return sorted(level_sum)[-k]
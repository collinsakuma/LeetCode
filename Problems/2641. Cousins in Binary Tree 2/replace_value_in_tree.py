from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root):
        # use m to sum each level
        m = Counter()

        def dfs(r, l):

            if not r: return

            m[l] += r.val
            dfs(r.left, l + 1)
            dfs(r.right, l + 1)
        # find the sum of the levels
        dfs(root, 0)

        # find the sum of the cousins and create new binary trees
        def dfs1(r, l, curr):
            sum_of_cousins = m[l + 1] - (r.left.val if r.left else 0) - (r.right.val if r.right else 0)
            if r.left:
                curr.left = TreeNode(sum_of_cousins)
                dfs1(r.left, l + 1, curr.left)
            if r.right:
                curr.right = TreeNode(sum_of_cousins)
                dfs1(r.right, l + 1, curr.right)
            return curr
        
        return dfs1(root, 0, TreeNode(0))
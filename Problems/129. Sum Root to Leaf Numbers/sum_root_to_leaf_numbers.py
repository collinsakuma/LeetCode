class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):

        def dfs(curr, num):
            if curr is None:
                return 0
            # accumulate the path of the nodes 
            num = num * 10 + curr.val

            # if no nodes left or right return the number
            if not curr.left and not curr.right:
                return num
            # recursively find the totals of the left and right nodes
            return dfs(curr.left, num) + dfs(curr.right, num)
    
        return dfs(root, 0)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root):
        # depth first search function
        # distribute coins if child has more coins give parent coins if parent has more coins distribute down to child
        def dfs(root, parent):
            if root == None:
                return 0
            moves = dfs(root.left, root) + dfs(root.right, root)
            x = root.val - 1
            if parent != None:
                parent.val += x
            moves += abs(x)

            return moves
        return dfs(root, None)
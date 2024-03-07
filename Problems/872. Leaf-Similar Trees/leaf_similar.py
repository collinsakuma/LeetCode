class Solution:
    def leafSimilar(self, root1, root2):
        # helper function
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            
            return dfs(root.left) + dfs(root.right)
        
        return dfs(root1) == dfs(root2)
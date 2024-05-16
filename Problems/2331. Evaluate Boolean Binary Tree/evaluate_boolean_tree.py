class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root):
        # use DFS
        def dfs(node):
            # if the node value is false return 0
            if node.val == 0:
                return 0
            # if the node value is true return 1
            elif node.val == 1:
                return 1
            # if the node is a the BOOLEAN opeartor OR recursively check its child nodes
            elif node.val == 2:
                # if one of the child nodes return true return 1
                if dfs(node.left) == 1 or dfs(node.right) == 1:
                    return 1
                # if both are false return false
                else:
                    return 0
            # if the node is the BOOLEAN operator AND recursively check its child nodes
            elif node.val == 3:
                # if both child nodes are true return 1
                if dfs(node.left) == 1 and dfs(node.right) == 1:
                    return 1
                # if at least one of the two child nodes is false return 0
                else:
                    return 0
                
        # use dfs() to check the entire binary tree
        return dfs(root)
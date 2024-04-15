class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        
        def dfs(node, is_left):
            # if not a node return no value
            if not node:
                return 0
            
            # if there are no nodes coming off of this node and this is a left node return its value
            if not node.left and not node.right and is_left:
                return node.val
            
            # get the sum of the left side nodes 
            left_sum = dfs(node.left, True)
            # get the sum of the right sum nodes 
            right_sum = dfs(node.right, False)

            # return the total sum of nodes
            return left_sum + right_sum
        
        return dfs(root, False)
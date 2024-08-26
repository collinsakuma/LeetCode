class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postOrderTraversal(self, root):
        order = []

        # recursive fuction to traverse nodes and append nodes in reverse order
        def traverse(node):
            # if not a node return 
            if node is None:
                return
            # recursively check left and right nodes
            traverse(node.left)
            traverse(node.right)
            # only after append the node value last
            order.append(node.val)

        # traverse from root
        traverse(root)

        # return the post order traversal 
        return order
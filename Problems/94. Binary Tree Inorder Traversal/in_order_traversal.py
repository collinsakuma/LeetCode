class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return inorder(root)
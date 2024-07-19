class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        s = set(to_delete)

        res = []

        def find(root, flag):
            if not root:
                return None
            delete = (root.val in s)
            root.left = find(root.left, delete)
            root.right = find(root.right, delete)

            if not delete and flag:
                res.append(root)

            return None if delete else root
        
        find(root, True)

        return res
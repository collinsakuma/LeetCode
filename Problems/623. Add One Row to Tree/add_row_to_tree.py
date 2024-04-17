class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addOneRow(self, root, val, depth, side='left'):
        # if the depth is one then create a new node and add the binary tree to the left node
        if depth == 1:
            output = TreeNode(val)
            setattr(output, side, root)
            return output
        # itterate though the tree decreasing depth untill it hits the insertion layer
        if root:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1, 'right')

        return root
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def smallestFromLeaf(self, root):
        self.output = None

        def dfs(root, path):
            if not root:
                return
            # add the values for the path from the leaf
            path.append(chr(root.val + ord('a')))

            # if there are no left or right nodes then a ndoe leaf has been reached
            if not root.left and not root.right:
                # reverse the order of the leaf
                rev_path = ''.join(path[::-1])
                # if a smallest leaf has not yet been set set a value
                # if there is already a smallest leaf check if current path is smaller
                if self.output is None or rev_path < self.output:
                    self.output = rev_path

            # check both the left and right paths from the node
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        
        dfs(root, [])

        return self.output
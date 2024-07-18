class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root, distance):
        # initilize a count of the good pairs
        self.pairs = 0

        # depth first search healper function
        def dfs(root):
            if not root:
                return []
            # if node only has one child node return depth of 1
            if not root.left and not root.right:
                return [1]

            # call dfs() function on the left and right sub trees
            left = dfs(root.left)
            right = dfs(root.right)

            # loop through the left and right lists to calculate the number of
            # pairs whose distance is less than the given distance
            for i in left:
                for j in right:
                    if i + j <= distance:
                        self.pairs += 1
            # return a list of distances from the current node to its descendants
            return [i + 1 for i in left + right if i + 1 < distance]
        
        dfs(root)

        return self.pairs
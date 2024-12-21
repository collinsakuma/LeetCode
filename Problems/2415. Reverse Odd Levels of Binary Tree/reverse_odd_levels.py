class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root):        
        tree = [root] # copy binary tree
        level = 0 # set starting level

        # traverse the tree nodes
        while tree:
            # increment the level
            level += 1
            # set a temporaty tree
            temp_tree = []
            # loop through the nodes in the tree
            for node in tree:
                # add the child nodes to the temp tree
                if node.left:
                    temp_tree += [node.left]
                if node.right:
                    temp_tree += [node.right]

            # if the level is an odd level of the tree reverse the nodes
            if level % 2 == 1:
                for i in range((len(temp_tree) + 1) // 2):
                    temp_tree[i].val, temp_tree[len(temp_tree) - i - 1]. val = temp_tree[len(temp_tree) - i - 1].val, temp_tree[i].val

            # set new tree
            tree = temp_tree
        
        return root
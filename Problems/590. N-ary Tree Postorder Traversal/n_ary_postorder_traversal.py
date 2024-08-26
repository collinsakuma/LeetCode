class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def post_orddr(self, root):
        # if not values are in the n ary tree return an empty list
        if not root:
            return []
        
        order = []

        # dfs helper traversal function
        def traverse(node):
            # if the node has no child nodes under it do nothing
            if not node.children:
                None
            # if there the nodes has children nodes, recurvicely traverse those nodes
            for child in node.children:
                traverse(child)
            # after child nodes have been recursively traversed append the value of the node
            # append at the end because we want a postorder (backwards)
            order.append(node.val)

        # start the traversal with the original node (root)
        traverse(root)

        # return the postorder traveral list of node values
        return order
class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root, startValue, destValue):
        # find the node the start or destination value
        def find(node, val, path):
            # if the value is found return true
            if node.val == val:
                return True
            # if there is a left branch from the node continue to search for the start/destination point
            if node.left and find(node.left, val, path):
                # add the path direction
                path += 'L'
            # if there is a right branch search for the value through the right branch
            elif node.right and find(node.right, val, path):
                # add the path direction
                path += 'R'
            # return the path
            return path
        
        # two paths from start and destination
        s, d = [], []

        # use the find function to find the start and destination nodes
        find(root, startValue, s)
        find(root, destValue, d)

        # loop through the two paths 
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()

        # turn the start list into U as it needs to traverse up the list to the lowest common ancestor node
        return ''.join('U' * len(s)) + ''.join(reversed(d))
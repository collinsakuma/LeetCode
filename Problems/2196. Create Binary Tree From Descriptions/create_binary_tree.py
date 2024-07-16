from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions):
        # store the nodes and their child nodes and if they are a left branch
        nodes = defaultdict(list)
        # use a dictionary to find the root node
        has_parent = {}
        root = TreeNode()

        # loop through descriptions
        for parent, child, is_left in descriptions:
            # add the child nodes and if it is a left node to the parent 
            nodes[parent].append([child, is_left])

            # find the root node
            if parent not in has_parent:
                has_parent[parent] = 0
            if child not in has_parent:
                has_parent[child] = 1
            else:
                has_parent[child] += 1

        # if the key(parnet) has no value then the root node has been found
        # initalize the nodelist
        for item in has_parent.items():
            if item[1] == 0:
                root = TreeNode(item[0])
                break
        
        # use a deque set first with the root node
        dq = deque([root])

        while dq:
            parent = dq.popleft()
            for kid, left in nodes.pop(parent.val, []):
                dq.append(TreeNode(kid))
                if left == 1:
                    parent.left = dq[-1]
                else:
                    parent.right = dq[-1]
        
        return root
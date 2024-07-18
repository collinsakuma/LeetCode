from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        # if there is no tree to traverse return an empty list
        if not root:
            return []
        
        # set an empty list to hold the level lists
        levels = []

        # set the tree into a deque
        q = deque([root])

        # while there are nodes in q
        while q:
            # create a level
            level = []
            # loop through a range of q
            for _ in range(len(q)):
                # pop the node
                node = q.popleft()
                # add the node values to the level list
                level += [node.val]
                # loop through the node if it has children and append the children to q
                for n in node.children:
                    q.append(n)
            # add the level to the levels list
            levels += [level]

        return levels
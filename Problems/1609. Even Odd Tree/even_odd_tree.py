class Solution:
    def isEvenOddTree(self, root):
        if root is None:
            return True
        queue = [root] # initalize queue with the root node
        level = 0

        while queue: # BFS traversal
            # initalize prev with negative infinity for even levels and positive infinity for odd levels
            prev = float('-inf') if level % 2 == 0 else float('inf')
            for _ in range(len(queue)): # iterate over nodes at current level
                node = queue.pop(0) # pop the first node from the queue
                # check conditions for even and odd levels
                if (level % 2 == 0 and (node.val % 2 == 0 or node.val <= prev)) or (level % 2 != 0 and (node.val % 2 != 0 or node.val >= prev)):
                    return False # return False if any condition not valid
                # add the left and right child node if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # update prev to the current nodes value
                prev = node.val
            # move to the next level
            level += 1
        return True
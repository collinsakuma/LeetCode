from collections import deque

class Solution:
    def findBottomLeftValue(self, root):
        queue = deque([root])
        leftmost = None

        while queue:
            leftmost = queue.popleft()
            if leftmost.right:
                queue.append(leftmost.right)
            if leftmost.left:
                queue.append(leftmost.left)
        
        return leftmost.val
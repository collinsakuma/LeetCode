class Solution:
    def rangeSumBST(self, root, low, high):
        stack, sum = [root], 0 # set a stack equal to the binary tree, with nodes in list form, also sum variable

        while stack: # while there are nodes in the stack continue the loop
            node = stack.pop() # pop the last node in the list and set it as its own variable
            if node: # if the node is not empty
                # first check if the node is greater than the lower end of the allowed range
                if node.val > low:
                    # if in range append node to the stack
                    stack.append(node.left)
                # second check if the node is less than the higher end of the allowed range
                if node.val < high:
                    # if in range append node to the stack
                    stack.append(node.right)
                if low <= node.val <= high: # if value is in the required range add the value to sum
                    sum += node.val      
        return sum
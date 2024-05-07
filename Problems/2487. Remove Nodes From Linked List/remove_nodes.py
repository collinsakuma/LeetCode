class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        curr = head
        stack = []

        while curr:
            # check if the next nodes value if greater than the current nodes
            while stack and stack[-1].val < curr.val:
                # if value is less than current node pop the value out of the stack
                stack.pop()
            # if new greater value found or stack is empty append the current node
            stack.append(curr)
            # set new current node
            curr = curr.next

        nxt = None

        while stack:
            curr = stack.pop()
            curr.next = nxt
            nxt = curr

        return curr
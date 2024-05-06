class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # set the val of the current node to the same value
        node.val = node.next.val
        # skip the next node and connect it to the one after
        node.next = node.next.next
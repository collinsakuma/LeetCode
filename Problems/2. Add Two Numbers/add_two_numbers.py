class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # create a dummy head infront of the list nodes
        dummy_head = cur = ListNode(0)
        # keep track of a carry value for carrying remainder
        carry = 0

        # loop while there are nodes in either list or their is still a remainder to carry to a node
        while l1 or l2 or carry:
            # while nodes still in l1
            # - add value of node to carry
            # - increment l1 to next node
            if l1:
                carry += l1.val
                l1 = l1.next
            # while nodes still in l2
            # - add value of node to carry
            # - increment l2 to next node
            if l2:
                carry += l2.val
                l2 = l2.next
            # set a next node value to the remainder of the carry by 10
            cur.next = ListNode(carry % 10)
            # increment cur to next
            cur = cur.next
            # set the remainer of the carry variable
            carry //= 10

        return dummy_head.next
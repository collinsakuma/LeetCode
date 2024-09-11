class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def insertGreatestCommonDivisors(self, head):
        # helper function to find the greatest common divisor
        def common_divisor(a, b):
            while b:
                a, b = b, a % b
            return a
        
        ans = ListNode(0)
        curr = ans

        # while still nodse in linked list
        while head.next:
            # find the greatest common divisor between adjacent nodes
            gcd_val = common_divisor(head.val, head.next.val)
            # set next to a new list node
            curr.next = ListNode(head.val)
            # set the next next node to the greatest common divisor
            curr.next.next = ListNode(gcd_val)

            # increment head and current node
            head = head.next
            curr = curr.next.next

        curr.next = ListNode(head.val)
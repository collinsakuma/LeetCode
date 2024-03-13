class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head):
        # create and point dummy node at the head of the list
        pointer = ListNode(float('inf'))
        pointer.next = head
        # create a reference to the list and point head to the dummy node
        curr = head
        head = pointer

        # loop over node
        while head:
            # track current sum
            current_sum = 0
            # for each node add to the consecutive sum
            while curr:
                # add the value of the node to the current sum
                current_sum += curr.val
                # if the consecutive sum is 0 delete the reference to the nodes that sum to 0
                if current_sum == 0:
                    head.next = curr.next
                # move to next node
                curr = curr.next
            # move the head
            head = head.next

            # update current node 
            if head:
                curr = head.next
        return pointer.next
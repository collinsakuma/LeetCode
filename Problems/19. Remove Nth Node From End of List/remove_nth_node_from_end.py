class Solution:
    def removeNthFromEnd(self, head, n):
        # set two pointers both equal to head
        fast, slow = head, head

        # loop through a range of n
        # give the fast pointer a head start of n nodes
        for _ in range(n):
            fast = fast.next

        # if fast == None then the linked list is of length n
        # if this is the case then the first node is the target node 
        # return head.next
        if not fast:
            return head.next
        
        # traverse the fast list untill the end
        while fast.next:
            # increment nodes for fast and slow
            fast, slow = fast.next, slow.next

        # when the fast linked list is finished being traversed 
        # slow.next will be the target node that needs to be removed
        # set the target node to the .next.next ( essentialy skipping the target node ) 
        slow.next = slow.next.next

        return head # return the linked list
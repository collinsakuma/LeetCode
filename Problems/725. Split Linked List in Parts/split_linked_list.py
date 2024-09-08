class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
        def splitListToParts(self, head, k):
            parts = [None] * k # list of ListNode pointers to store k parts

            len = 0
            node = head
            # calculate the length of the linked list
            while node:
                len += 1
                node = node.next
            
            # calculate the minimum size of each part
            n, r = divmod(len, k)

            # reset pointer to begining of the linked list
            node = head
            prev = None

            # loop through each part
            for i in range(k):
                # add node to start of the current part
                parts[i] = node
                # loop through n + 1 nodes if there are remaining extra nodes
                # else only traverse n nodes
                for _ in range(n + (1 if r > 0 else 0)):
                    prev = node
                    node = node.next
                # disconnect current part form the rest of the list
                if prev:
                     prev.next = None
                # decrement count of extra nodes
                if r > 0:
                     r -= 1
        
            return parts

                
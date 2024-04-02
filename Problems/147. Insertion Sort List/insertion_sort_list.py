class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):

        # edge case for an empty list, or list of length 1
        if not head or not head.next:
            return head
        
        # dummy_head will ally for insertion ahead of head easliy
        dummy_head = ListNode(val=-5000, next=head)
        # last node to be sorted
        last_sorted = head
        # curr is next node of last_sorted
        curr = head.next

        while curr:
            # if the current nodes value is greater than the last sorted nodes value, then it does not need to be moved in the linked list
            if curr.val >= last_sorted.val:
                # increment last_sorted to the next node
                last_sorted = last_sorted.next
            # curr needs to be moved to a further forward position in the linked list
            else:
                # search for position to insert curr
                prev = dummy_head
                # loop though linked list untill the next node is less than curr nodes value
                while prev.next.val <= curr.val:
                    # traverse list while in loop
                    prev = prev.next
                # set a new last_sorted node
                last_sorted.next = curr.next 
                # insert the node into the linked list
                curr.next = prev.next
                # update the next refference of prev to point to curr node
                prev.next = curr
            # update the curr pointer to point to the next node after the last sorted node ( next node to be sorted )
            curr = last_sorted.next

        return dummy_head.next
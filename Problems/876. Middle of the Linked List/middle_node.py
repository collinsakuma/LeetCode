class Solution:
    def middleNode(self, head):
        # set two pointers equal to the head of the linked list
        slow = fast = head

        # while there are still nodes in fast continue to loop
        while fast:
            # increment fast to the next node first
            fast = fast.next
            # if there are no more nodes present in fast break from the loop
            if not fast:
                break
            else: # else increment fast a second time
                fast = fast.next

            # increment slow pointer only one node per loop
            slow = slow.next
        
        return slow # return the middle node
            
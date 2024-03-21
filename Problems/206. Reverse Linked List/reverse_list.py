class Solution:
    def reverseList(self, head):
        # set a previous variable to none 
        prev = None
        # set current node to the head node of the linked list
        current = head

        # loop though the linked list untill the end
        while current != None:
            # set a next variable to the next node
            next = current.next
            # set the next node to the previous node in the list
            current.next = prev
            # set a new previous node to the current one for the next loop
            prev = current
            # set the current node to the next one in the linked list
            current = next
            # set new head ( building the linked list in reverse order )
            head = prev

        return head
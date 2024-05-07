class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head):
        # use the reverse() function to reverse the order of the linked list
        reversed_list = self.reverse(head)
        # track the carry amount for the previous node
        carry = 0
        current, previous = reversed_list, None

        # traverse the reversed linked list
        while current:
            # find the new value for the current node
            new_value = current.val * 2 + carry
            # updae the current nodes value
            current.val = new_value % 10
            # check if there is a carry value for the next iteration
            carry = 1 if new_value > 9 else 0
            # move to the next nodes
            previous, current = current, current.next

        # if there is a carry after traversing the list add an extra node
        if carry:
            previous.next = ListNode(carry)
        
        # reverse th list again to the original order
        result = self. reverse(reversed_list)

        return result

    def reverse(self, node):
        previous, current = None, node
        
        # traverse the linked list
        while current:
            # store next node
            next_node = current.next
            # reverse the link
            current.next = previous
            # move to next nodes
            previous, current = current, next_node
        # previous becomes the new head of the reversed list
        return previous
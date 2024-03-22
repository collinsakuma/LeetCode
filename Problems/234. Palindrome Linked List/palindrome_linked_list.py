import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # create a deepy cody of head linked list that will not change when head is modified
        deep_copy_of_head = copy.deepcopy(head)

        #### code bellow to reverese the order of the linked list ####
        prev = None # set previous node value to None
        current = head # set current value to the head of the linked list

        # while current node does not equal None ( traverse till the end of the linked list )
        while current != None:
            # set next variable to next node in the list
            next = current.next
            # set the next node to the previous nodes value
            current.next = prev
            # set a new prev node value to the current
            prev = current
            # set a new current value to the next node in the linked list
            current = next
            # set head to prev value
            head = prev

        # travers though the deep copy of head and the reveresed head linked list together
        while deep_copy_of_head.next != None:
            # if the values do not match the the linked list is not palandromic
            if deep_copy_of_head.val != head.val:
                return False
            else: # traverse lists till their end of untill False condition is found
                deep_copy_of_head = deep_copy_of_head.next
                head = head.next

        return True

        
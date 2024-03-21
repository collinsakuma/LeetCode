class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        # set the two pointers
        pointer1 = list1
        pointer2 = list1
        i, j = 0, 0

        # loop through pointer1 to get to node before a
        while i != a - 1:
            pointer1 = pointer1.next
            i += 1

        # loop through pointer2 to reach node  b
        while j != b:
            pointer2 = pointer2.next
            j += 1

        # connect list2 to the next of pointer1 (I.E. pointer1 --> node of list2)
        pointer1.next = list2

        # traverse the list2 till the end
        while list2.next != None:
            list2 = list2.next
        
        # connect the remaining part of list1 to list2
        list2.next = pointer2.next

        return list1
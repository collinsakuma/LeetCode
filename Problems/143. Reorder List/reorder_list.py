
class Solution:
    def reorderList(self, head):

        arr = []

        cur, length = head, 0

        # save the linked list into an array
        while cur:
            arr.append(cur)
            cur, length = cur.next, length + 1
            
        left, right = 0, length - 1
        last = head

        # reorder the linked list with two pointers
        while left < right:
            arr[left].next = arr[right]
            left += 1

            if left == right:
                last = arr[right]
                break
            arr[right].next = arr[left]
            right -= 1

            last = arr[left]

        if last:
            last.next = None
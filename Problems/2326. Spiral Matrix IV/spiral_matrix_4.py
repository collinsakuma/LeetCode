class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def spiralMatrix(self, m, n, head):
        # create the two d matrix
        matrix = [[-1] * n for _ in range(m)]

        current = head # set current to head
        direction = 1 # set the starting direction
        i, j = 0, -1 # set initial coordinates, j == -1 becuase first direction should be j += 1

        # while there are values in the linked list
        while current:
            # loop through a range of n
            for _ in range(n):
                # if values still in linked list
                if current:
                    # increment j by the direction
                    j += direction
                    # set the coordaintes to the current value in the linked list
                    matrix[i][j] = current.val
                    # traverse to the next node in the linked list
                    current = current.next

            m -= 1 # decrement m by 1 because the first row has been filled out

            # loop through range of columns
            for _ in range(m):
                if current: # increment i value by directions
                    i += direction
                    # set coordinates to the current value of the linked list
                    matrix[i][j] = current.val
                    # traverse to next value in the linked list
                    current = current.next

            n -= 1 # reduce the count of columns by 1 as one has been filled

            direction *= -1

        return matrix
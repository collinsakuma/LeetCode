import heapq

class Solution:
    def halveArray(self, nums):
        # find the target sum that must be reached
        target = sum(nums) / 2
        operations = 0

        # put numbers in a priority que in reverse order
        heap = [-num for num in nums]
        heapq.heapify(heap)

        # while the sum of the arrays still greater than target
        while target > 0:
            # pop the smallest item from the heap and convert to a posivite number, becuase nums are stored in the heap 
            # as negative numbers the smallest one is actually the largest number
            num = -heapq.heappop(heap)
            # divide the target num in half
            num /= 2
            # reduce target sum by num
            target -= num
            # push the reduced number back into the heap conveting it back into a negative number
            heapq.heappush(heap, -num)
            # increment operation ammount
            operations += 1
        
        return operations
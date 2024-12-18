import heapq
class Solution:
    def getFinalState(self, nums, k, multiplier):
        # create heap of num and its index
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        # loop through range of operations
        for x in range(k):
            x, i = heap[0]
            # replace heap with new number modified by the multiplier
            heapq.heapreplace(heap, (x * multiplier, i))

        for x, i in heap:
            nums[i] = x
        
        return nums
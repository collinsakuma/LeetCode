import heapq
class Solution:
    def getFinalState(self, nums, k, multiplier):
        heap = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(heap)

        for x in range(k):
            x, i = heap[0]
            heapq.heapreplace(heap, (x * multiplier, i))

        for x, i in heap:
            nums[i] = x
        
        return nums
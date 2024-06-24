import heapq

class Solution:
    def longestSubarray(self, nums, limit):
        max_length = 1

        for i in range(len(nums)):
            max_heap = [-nums[i]]
            min_heap = [nums[i]]

            for j in range(i + 1, len(nums)):
                if abs(-max_heap[0] - nums[j]) <= limit and abs(min_heap[0] - nums[j]) <= limit:
                    heapq.heappush(max_heap, -nums[j])
                    heapq.heappush(min_heap, nums[j])
                else:
                    break
                max_length = max(len(max_heap), max_length)
            
        return max_length
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums, k):
        frequency = defautdict(int)
        n = len(nums)

        i, j, output = 0, 0, 1

        while i < n and j < n:
            # while the element on the right side of the window appears more than k times
            while frequency[nums[j]] > k:
                # remove the left most element at index i and increment the sliding window
                frequency[nums[i]] -= 1
                i += 1
            # after each movement of the window check if there is a new longest subarray 
            output = max(output, j - 1 + 1)
            # expand the right side of the sliding window right
            j += 1
        # return the longest subarray length
        return output
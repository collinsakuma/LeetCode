from functools import reduce
import operator

class Solution:
    # first solution TIME LIMIT EXCEEDED, runs too slow
    def numSubarrayProductLessThanK(self, nums, k):
        output = 0

        for i in range(len(nums)):
            window = i + 1
            while window <= len(nums):
                if reduce(operator.mul, nums[i:window], 1) < k:
                    output += 1
                else:
                    break
                window += 1

        return output
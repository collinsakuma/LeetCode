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
    
    # sliding window approach
    def numSubarrayProductLessThanKTWo(self, nums, k):
        # edge case if k is less than or equal to 1 then there can be no subarrays who's product is less than that
        if k <= 1:
            return 0
        
        # set left and right to represent the sliding window
        # set the product to keep track of the product of the elements currently in the window
        # set the count to track how many subarrays are found who's product is < k
        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            # increase the product by the right side of the sliding window
            product *= nums[right]
            # if the product is greater than or equal to k slide the left side of the window
            while product >= k:
                # divide product by the elements leaving the window as it slides right
                product //= nums[left]
                left += 1 # increment left side
            # increase count by the number of subarrays within current window
            count += 1 + (right - left)
            right += 1 # increment right

        return count
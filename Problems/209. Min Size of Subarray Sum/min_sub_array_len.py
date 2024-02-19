class Solution:
    def minSubArrayLen(self, target, nums):
        # set two pointers
        left, right, total = 0, 0, 0
        # min length to be length of array plus 1 ( for an invalid min_length )
        min_len = len(nums) + 1

        # loop through the array
        while right < len(nums):
            # add current number to sum
            total += nums[right]
            # move right pointer
            right += 1

            # check if sum is greater than or equal to target
            while total >= target:
                # update minimum length if necessary
                min_len = min(min_len, right - left)
                # subtract left number from the sum and move left pointer
                total -= nums[left]
                left += 1

        # if min_len is still the initalized value then no valid subarray exist
        if min_len == len(nums) + 1:
            return 0
        else: 
            return min_len
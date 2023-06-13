class Solution:
    def minOperations(self, nums):
        count = 0 # set a begining counter to keep track of number of operations
        for i in range(1, len(nums)):
            # start a loop that starts at the second element (index 1 instead of 0)
            if nums[i] <= nums[i - 1]:
                # if index at nums[i] is greater than the number at the index before
                x = nums[i]
                nums[i] += (nums[i-1] - nums[i]) +1
                # add the difference between the previous index + 1
                # Example 
                # - if nums[i] = 5 and nums[i-1] = 10
                # - 5 += (10 - 5) + 1
                # - nums[i] then becomes 11
                count += nums[i] - x
                # add the amount of operations it took to make nums[i] greater than nums[i-1]
                # in the example about it would be count += 11 - 5
        return count
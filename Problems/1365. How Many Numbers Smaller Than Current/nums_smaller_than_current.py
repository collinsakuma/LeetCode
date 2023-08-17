class Solution:
    def smallerNumbersThanCurrent(self, nums):

        smaller = [0] * len(nums) # create a array of equal length to nums to represent numbers smaller
        sorted_nums = sorted(nums) # sorted version of the nums array

        for i in range(len(nums)): # loop though range of len(nums)
            smaller[i] = sorted_nums.index(nums[i]) # for each number in nums, set the value of output array to the positon of each number in sorted
            # this represents how many numbers are smaller than itself
        return smaller
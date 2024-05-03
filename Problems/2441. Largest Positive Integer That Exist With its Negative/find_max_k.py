class Solution:
    def findMaxK(self, nums):
        # loop through a sorted list of nums in reverse order ( from highest to lowest )
        for num in sorted(nums, reverse=True):
            # if the negative of num is in nums return num
            if -num in nums:
                return num
        # if no negative complement of a number is found return -1
        return -1
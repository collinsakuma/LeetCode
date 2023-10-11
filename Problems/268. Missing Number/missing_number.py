class Solution:
    def missingNumber(self, nums):
        # loop through range of length of nums plus 1 because there is one missing number
        for i in range(len(nums) + 1):
            if i not in nums: # check for the missing numbers
                # when missing number is found return the number
                return i
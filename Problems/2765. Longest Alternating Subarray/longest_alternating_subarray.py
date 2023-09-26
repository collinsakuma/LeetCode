class Solution:
    def alternatingSubarray(self, nums):
        longest = -1 # set initial value of longest subarray at -1

        for i in range(len(nums)): # loop though range of length nums
            # second loop from i + 1 to len nums
            for j in range(i + 1, len(nums)):
                # check if nums[j - 1] ( number previous ) is not equal to nums[j]  + -1 ** j - i (-1 ** j -1 will return -1 or 1 depending on if index is positive or negative)
                if nums[j - 1] != nums[j] + (-1)**(j - i):
                    # if values not equal break from current loop as conditions have not been met
                    break
                # check if a new longest current subarray has been found that meet the conditions, if so set new longest
                longest = max(longest, j - i + 1)
            return longest
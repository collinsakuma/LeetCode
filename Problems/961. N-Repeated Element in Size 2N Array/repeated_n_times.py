class Solution:
    def repeatedNTimes(self, nums):
        for num in set(nums): # loop though a list of unique numbers in num
            if nums.count(num) == len(nums) / 2: # check if each num has the count of n in nums
                return num # return num if true
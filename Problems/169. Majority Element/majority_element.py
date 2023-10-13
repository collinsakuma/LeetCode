class Solution:
    def majorityElement(self, nums):
        for num in set(nums): # loop though a set of unique numbers in nums
            # count how many times num is in numbers, if it occures more than the length of nums / 2 return that number
            if nums.count(num) > len(nums) / 2:
                return num
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        s = s * (n + 1) // 2 # will calculate the sum of 1 to n, including the missing number
        missing = s - sum(set(nums)) # find what the missing number is by finding the sum of the set() - what the sum should be (s)
        duplicate = sum(nums) + missing - s # find the number that is duplicated in the list

        return [duplicate, missing] # return the duplicate and missing number in list format
    
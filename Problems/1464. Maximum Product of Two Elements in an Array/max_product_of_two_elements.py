class Solution:
    def maxProduct(self, nums):
        nums = sorted(nums) # sort nums from smallest to largest
        return (nums[-1] - 1) * (nums[-2] - 1) # find the product of the two elements at the end of the list 
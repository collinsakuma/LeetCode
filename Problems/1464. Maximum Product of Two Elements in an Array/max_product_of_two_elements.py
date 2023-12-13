class Solution:
    def maxProduct(self, nums):
        nums = sorted(nums) # sort nums from smallest to largest
        return (nums[-1] - 1) * (nums[-2] - 1) # find the product of the two elements at the end of the list 
    
    def maxProductTWo(self, nums):
        # set two points
        first, second = 0, 0

        for num in nums: # loop through nums
            if num >= first: # check if num is greater than or equal to first, if num is greater set new first and second variables
                second, first = first, num
            elif num >= second: # if num is not greater than first check if it is greater than second, if greater set new second value
                second = num
        
        return (first - 1) * (second - 1)
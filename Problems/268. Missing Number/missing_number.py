class Solution:
    def missingNumber(self, nums):
        # loop through range of length of nums plus 1 because there is one missing number
        for i in range(len(nums) + 1):
            if i not in nums: # check for the missing numbers
                # when missing number is found return the number
                return i
            
    def missingNumberTwo(self, nums):
        # only one number is missing from the list nums
        # take the sum of the range of len nums + 1
        # take the sum of the nums given
        # the difference between the two is the missing number from the list nums
        return sum(range(len(nums) + 1)) - sum(nums)
    
    def missingNumberThree(self, nums):
        total = sum(range(len(nums) + 1)) # total what the sum in range of nums plus the missing number should be
        nums_sum = sum(nums) # total of nums ( missing the number )
        
        return total - nums_sum #return the missing number
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        solution = [1] * length # create a solutions array the same length as the original array
        pre_sum = 1 # set a presum variable to keep track of the product before the current number
        post_sum = 1 # set a post sum variable to keep track of the product after the variable.

        for i in range(length): # loop though the range of the length nums
            solution[i] *= pre_sum # multiply the index in the solution list by the sum of the previous indexes of nums
            pre_sum = pre_sum * nums[i] # change the new pre_sum by multiplying it by the current index
            solution[length - i - 1] *= post_sum # iterating backwards set the solution 
            post_sum = post_sum * nums[length - i - 1]
        
        return solution
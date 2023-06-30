class Solution:
    def arrayPairSum(self, nums):
        sorted_nums = sorted(nums) # sort the list of nums
        output = 0 # create a variable that will keep track of the sum of the min pairs

        for i in range(0, len(nums) - 1, 2): # loop though nums by 2
            output += min(sorted_nums[i], sorted_nums[i + 1]) # add the min of each pair to the output
        return output # return the maximum output of min pairs
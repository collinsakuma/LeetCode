class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums: # if not nums in nums there is no pattern that can be formed return 
            return 0
        
        # set initial values of current length and max length to 1
        curr_length = 1
        max_length = 1

        for i in range(1, len(nums)): # loop though range of lenght nums starting at the second index
            if nums[i] > nums[i - 1]: # check if num at index i is greater than the number at the index before, if not it cannot be an increasing index
                curr_length += 1 
            else: # if in an increasing subsequence
                max_length = max(max_length, curr_length) # check if the curr_length is greater than the current max length if so set new max length
                curr_length = 1 # reset the current length back to 1
        
        return max(max_length, curr_length)
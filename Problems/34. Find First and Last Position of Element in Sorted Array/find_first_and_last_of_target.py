class Solution:
    def searchRange(self, nums, target):
        output = [-1, -1] # first and last indexs for target value, -1, -1 default if no match is found

        # loop through range forward
        for i in range(len(nums)):
            if nums[i] == target: # if num at index i equals target set first element in ouput to i
                output[0] == i
                break # break from loop as first instance has been found
        
        # loop though range in reverse order
        for j in range(len(nums) - 1, -1, -1):
            if nums[j]  == target: # if num at index j equals target set last element in output to j
                output[1] = j
                break # break from loop as last instance of target has been found
        
        return output # return the output
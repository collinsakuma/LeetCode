class Solution:
    def divideArray(self, nums, k):
        output = [] # empty array 
        nums.sort() # sort the list in assending order
        for i in range(3, len(nums) + 3, 3): # loop through the lenght of range nums in increments of 3
            if nums[i - 1] - nums[i - 3] <= k: # check if the difference between the first number and the last number in the sequence has a difference greater than k
                # if the difference is less than or equal to k append the subarray to output
                output.append([nums[i - 3], nums[i - 2], nums[i - 1]])
            else: # if the difference is greater than k then it does not satisfy the conditions return an empty list
                return []
        return output # return the 2D matrix
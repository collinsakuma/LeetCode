class Solution:
    def isMonotonic(self, nums):
        # set two variables or increase and decrease to True at the begining and change depending on array
        increase = True
        decrease = True

        for i in range(1, len(nums)): # loop through range of len nums
            if nums[i] < nums[i - 1]: # if value at index i is less than value at the previous index then the array is not increasing
                increase = False # set increasing to False
            
            if nums[i] > nums[i - 1]: # if value at index i is greater than value at previous index then array is not decreasing
                decrease = False # set decreasing to false
        
        return increase or decrease # return True if either increase or decrease if true, return false is neither is true
class Solution:
    def largestPerimeter(self, nums):
        nums.sort() # sort the list 
        p = 0
        sum = nums[0] + nums[1] # sum of the lowest 2 numbers in the list

        for i in nums[2:]: # loop through the remaining numbers
            if sum > i: # if the current sum is greater than the current element
                p = sum + i # add element to the sum and set a new p
            sum += i

        if p == 0: # if p = 0 then there is no valild 3 sidded polygon
            return -1
        else:
            return p
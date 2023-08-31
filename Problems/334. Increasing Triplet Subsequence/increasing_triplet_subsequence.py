import math

class Solution:
    def increasingTriplet(self, nums):
        # set two variables first and second, first must come before second and be less than it
        first = math.inf
        second = math.inf

        for num in nums: # loop through list
            if num <= first: # if num is less than first replace first with new lower number
                first = num
            elif num <= second: # if num is greater than first but less than second replace second with new number
                second = num
            else: # if number is greater than first and greater than second the condition has been meet, first < second < num
                return True #return True
        return False 
import math 

class Solution:
    def arraySign(self, nums):
        if math.prod(nums) > 0: # if product is positive return 1
            return 1
        elif math.prod(nums) < 0: # if product is negative return -1
            return -1
        
        return 0 # if product equals 0 return 0
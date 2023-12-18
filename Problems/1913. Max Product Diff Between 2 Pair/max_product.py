import math

class Solution:
    def maxProductDifference(self, nums):
        sorted_nums = sorted(nums)
        
        return (sorted_nums[-1] * sorted_nums[-2]) - (sorted_nums[0] * sorted_nums[1])
        # want the difference between the product of the two largest numbers and two smallest numbers
        # 1. sort the array using sorted()
        # 2. (a, b) use the two numbers at the end of the sorted array index -1, -2
        # 3. (c, d) use the two smallest numbers at the begining of the array 0, 1
        # 4. return the largest difference possible. 


    def maxProductDifferenceTwo(self, nums):
        # set 4 variables for  the min 1 & 2 lowest number to choose
        # and max 1 & 2 highest numbers to choose set to infinity and negative infinity 
        min1 = min2 = math.inf
        max1 = max2 = -(math.inf)

        for n in nums: # loop though numbers in list nums
            # check for lowest possible numbers
            if n <= min1: # if current number is less than min1, set new min1 and min2
                min1, min2 = n, min1
            elif n < min2: # if not lower than min1, check if n is lower than min2
                min2 = n
            
            # check for highest possible numbers
            if n >= max1: # if n is greater than or equal to current max1, set new max1 and max2
                max1, max2 = n, max1
            elif n > max2: # if not greater than max1, check if greater than max2
                max2 = n
            
        return max1 * max2 - min1 * min2
import Math

class Solution:
    def findClosestNumber(self, nums):
        closest = Math.inf # set closest to infinity as its initial value

        for num in nums: # loop though all of the numbers in nums
            if abs(num) < abs(closest): # check if the absolute value of num is less than absolute value of closest, check absolute value because it doesnt matter if number is negative or not
                # if num is closer to 0 than closest set new closest
                closest = num
                # check if num and closest are the same
            elif abs(num) == abs(closest):
                # set closest to the greater of the two, I.E. if one of them is negative set closest to the positive value
                closest = max(num, closest)
        
        return closest # return closest number to 0
class Solution:
    def maximumCount(self, nums):
        neg, pos = 0, 0 # set two variables to keep track of the number of positive and negative numbers in list
        for num  in nums: # loop through nums
            # count the negative and positive numbers 
            if num < 0: 
                neg += 1
            elif num > 0:
                pos += 1
        return max(neg, pos) # return neg or pos, whichever is higher
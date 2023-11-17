class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # keep track of the max number of consecutive ones and current count of consecutive ones
        max_consecutive = 0
        curr_consecutive = 0

        for num in nums: # loop though list of nums
            if num != 1: # if consecutive 1's is broke, check if there is a new_maxconsecutive
                max_consecutive = max(max_consecutive, curr_consecutive)
                curr_consecutive = 0 # reset curr_consecutive to 0
            else:
                curr_consecutive += 1 # consecutive 1 increase count of consecutive 1's 

        return max(max_consecutive, curr_consecutive) # return the max number of consecutive 1's in the list nums
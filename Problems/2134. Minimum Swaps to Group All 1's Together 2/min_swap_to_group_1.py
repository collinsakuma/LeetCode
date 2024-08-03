import math

class Solution:
    def minSwap(self, nums):
        n = len(nums)
        min_moves = math.inf # set initial value of the minium moves to infinity
        count_ones = nums.count(1) # count of the number of ones in the list

        # concatenate nums to nums to connect the end to the begining
        nums = nums + nums

        count_zero = 0 # track the count of zeros in the window
        a = 0 # left side window starts at 0 index

        # loop through range of n plus the count of ones to account for circular list
        for i in range(n + count_ones):
            if nums[i] == 0: # if num at index i is 0 increase count of 0
                count_zero += 1
            # if we need to slide the left side of the window over check if the index
            # moving outside of the window is a zero, decrease count if necessary
            if i - a >= count_ones:
                if nums[a] == 0:
                    count_zero -= 1
                # slide window left
                a += 1
            # if the window of the same length as the number of ones in the list, 
            # check if the window represents a minimum amount of moves needed for
            # all 1's to be moved consecutively
            if i >= count_ones:
                min_moves = min(min_moves, count_zero)

        return min_moves
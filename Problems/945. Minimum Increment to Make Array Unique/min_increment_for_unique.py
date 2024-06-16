class Solution:
    def minIncrementForUnique(self, nums):
        moves = 0 # initialize moves count
        nums = sorted(nums) # sort list
        prev = nums[0] # set the initial value of the nums list

        # loop through range of nums skipping prev index set above
        for i in range(1, len(nums)):
            # if index i is less than or equal to prev number it needs to be incremented
            if nums[i] <= prev:
                # increment moves up the necessary amount to make index i
                # a unique number and higher than prev
                moves += prev + 1 - nums[i]
                # set new value for index i
                nums[i] = prev + 1
            # increment prev number
            prev = nums[i]
        return moves
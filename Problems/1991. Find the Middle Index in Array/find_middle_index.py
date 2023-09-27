class Solution:
    def findMiddleIndex(self, nums):
        # loop though range of length nums
        for i in range(len(nums)):
            # create two subarrays
            # - one for the numbers to the left of i
            # - another for the numbers to the right of i
            left = nums[:i]
            right = nums[i + 1:]
            # check if the sums of the two subarrays are the same
            # if so return i, i is the "middle index"
            if sum(left) == sum(right):
                return i
        return -1 # if no middle index is found return -1
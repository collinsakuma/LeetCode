class Solution:
    def pivotIndex(self, nums):
        for i in range(len(nums) - 1):
            # find sum of to the left and right of the current index i
            sum_left = sum(nums[:i])
            sum_right = sum(nums[i + 1:])
            if sum_left == sum_right: # if the sums are the same the pivot index has been found return i
                return i
        # check edge case if sum of all numbers to the left of the right index = 0
        if sum(nums[:len(nums) - 1]) == 0:
            return len(nums) - 1 # return the last index if sum equals 0
        return -1 # if no pivot index found return -1
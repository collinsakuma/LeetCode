class Solution:
    def sortedSquares(self, nums):
        # loop though nums, tracking index and value with enumerate()
        for i, num in enumerate(nums):
            # replace value at index i with a squared absolute value of num
            nums[i] = abs(num) ** 2

        return sorted(nums) # sort the array and return it
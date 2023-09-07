class Solution:
    def longestSubarray(self, nums):
        # set left and right side window to 0
        # zeros represents the number of zeros in the window at any given time
        zeros = left = right = 0

        for right in range(len(nums)):
            if nums[right] == 0: # if right side element is zero, increment zeros count by 1
                zeros += 1
            if zeros > 1: # if there are more than one zero in the window move the window right
                if nums[left] == 0: # if the left most number is 0, reduce the count of zeros by 1
                    zeros -= 1
                left += 1 # regardless of if left most element is 0 increment left, move window right
        return right - left
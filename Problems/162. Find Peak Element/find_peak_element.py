class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            # set mid as right biased ( left = mid in else condition )
            mid = left + ((right - left + 1) // 2)
            # if the potential mid peak is greater than the previous number
            # set left to mid ( new potential peak )
            if nums[mid] > nums[mid - 1]:
                left = mid
            # mid is less than previous number set new right bound
            else:
                right = mid - 1
        
        return left
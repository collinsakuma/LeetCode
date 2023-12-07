class Solution:
    def findMin(self, nums):
        # initialize two pointers one at begining one at end
        low, high = 0, len(nums) - 1

        while low <= high:
            if nums[low] <= nums[high]: # determine if nums is rotated or not
                return nums[low]
            
            mid = (low + high) // 2 # find the mid point between low and high

            if nums[low] > nums[mid]: # if nums[low] is greater than at midpoint between low and high then we must traverse left
                high = mid # set high point to mid keep low the same

            else: # we must traverse right
                # set low to mid keeping high pointer the same
                low = mid + 1 
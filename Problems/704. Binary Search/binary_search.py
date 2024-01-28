class Solution:
    def search(self, nums, target):
        # set the two points of the binary search
        low, high = 0, len(nums) - 1

        while low <= high: # while low point is less than or equal to high continue the loop
            mid = (low + high) // 2 # find the mid point between low and high
            if nums[mid] == target: # value at index mid is equal to target return the index of the target
                return mid
            elif nums[mid] > target: # if mid point is greater than the target set a new high boundary
                high = mid - 1
            else:
                low = mid + 1 # if the mid point is less than the target set a new low boundary

        return -1 # if target isnt in the list of nums return -1
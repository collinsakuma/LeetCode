class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
        # if the target number is in the list of numbers return index where that number is in the nums list
            return nums.index(target)
        else: 
        # if the target number is not in the list add that number to the list.
            nums.append(target)
        return sorted(nums).index(target)
        # sort the list with the added target number and find its index in the sorted list.
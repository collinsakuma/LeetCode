class Solution:
    def search(self, nums, target):
        if target not in nums: # it target number not in nums return -1
            return -1
        return nums.index(target) # find the index that has the same value as the target value
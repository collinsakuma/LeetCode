class Solution:
    def minimumDifference(self, nums, k):
        if len(nums) <= 1:
            return 0

        nums = sorted(nums) # sort numbers
        res = nums[k-1] - nums[0] # differene between lowest and lowest in sub list of k scores

        for i in range(k, len(nums)): # loop though range of k to end of sorted numbers
            res = min(res, nums[i] - nums[i - k + 1]) # update response if new minimum is found

        return res
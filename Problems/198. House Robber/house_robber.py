class Solution:
    def rob(self, nums):
        # edge cases where only 1 or 0 houses can be robbed
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        dp = [0] * len(nums) # set up the dp equal to length numbers
        # first two in dp list can only be set houses
        dp[0] = nums[0] 
        dp[1] = max(nums[0], nums[1])

        # loop through range from the second index
        for i in range(2, len(nums)):
            # for i in the range check which house is the best one to rob from
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
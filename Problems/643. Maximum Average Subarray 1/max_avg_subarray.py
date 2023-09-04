class Solution:
    def findMaxAverage(self, nums, k):
        curr_sum = max_sum = sum(nums[:k]) # first sum of the first interfal of k numbers

        for i in range(k, len(nums)): # loop though range of len nums
            curr_sum += nums[i] - nums[i - k] # find the curr sum adding the new interval at i and subtracting the number at the beging of the set of k nums
            max_sum = max(max_sum, curr_sum) # if curr_sum is greater than max_sum set a new max_sum

        return max_sum / k # find the average of max sum by dividing by k
class Solution:
    ## first solution gets TLE with longer test cases
    def maximumSubarraySum(self, nums, k):
        max_subarray = 0 # maintain max length of subarray

        # loop through range of nums minus k
        for i in range(len(nums) - k + 1):
            # if there are no duplicate numbers in the subarray length k
            if len(set(nums[i:i+k])) == k:
                # check if its sum is a new max_subarray sum
                max_subarray = max(max_subarray, sum(max_subarray))

        return max_subarray # return the max sum of a subarray of length k
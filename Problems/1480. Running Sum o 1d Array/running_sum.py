class Solution:
    def runningSum(self, nums):
        run_sum = []

        for i in range(1, len(nums) + 1): # loop through range of 1 to len(nums) + 1 to account for the 0 index
            # in each loop append the sum of nums from index 0 to i, each iteration will incresae the number of indexes summed by 1
            run_sum.append(sum(nums[:i]))
        return run_sum
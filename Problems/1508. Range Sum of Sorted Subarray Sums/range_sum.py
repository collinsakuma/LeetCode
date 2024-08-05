class Solution:
    def rangeSum(self, nums, n, left, right):
        output = []

        # loop through range of nums
        for i in range(len(nums)):
            # set the intial prefix sum
            prefix = 0
            # loop through range of nums from i to end 
            for j in range(i, len(nums)):
                # add the value to the prefix sum 
                prefix += nums[j]
                # append the prefix sum
                output.append(prefix)

        output.sort() # sort the list

        # find the accumulated sum between left and right point
        return sum(output[left - 1:right]) % (10**9 + 7)
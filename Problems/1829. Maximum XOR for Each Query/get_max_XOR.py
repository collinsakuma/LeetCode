class Solution:
    def getMaximumXor(self, nums, maximumBit):
        # create prefix sum array
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[len(prefix_sum) - 1] ^ nums[i])
        
        comp = 2 ** maximumBit
        ans = []

        for i in range(len(prefix_sum) - 1, -1, -1):
            current_res = prefix_sum[i]
            res = current_res ^ (comp - 1)
            ans.append(res)

        return ans
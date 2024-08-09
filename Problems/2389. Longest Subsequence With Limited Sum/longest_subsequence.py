class Solution:
    def answerQueries(self, nums, queries):
        nums.sort() # sort the numberes

        # create a array to hold the prefix sum when adding up the numbers
        prefix_sum = [0] * (len(nums) + 1)

        # loop through range of the list of numbers
        for i in range(len(nums)):
            # fill out the prefix sum list
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]

        ans = []

        for query in queries:
            i = 0

            while i < len(nums) and prefix_sum[i] + 1 <= query:
                i += 1
            ans.append(i)

        return ans
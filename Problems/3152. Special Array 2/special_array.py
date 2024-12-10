class Solution:
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        # create prefix sum
        prefix_sum = [0] * (n + 1)

        # loop through and create a prefix sum of non intersecting arrays
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix_sum[i] += 1


        output = []

        # check if each query is a special array
        for x, y in queries:
            if x == y:
                output.append(True)
            else:
                if prefix_sum[y] - prefix_sum[x] > 0:
                    output.append(False)
                else:
                    output.append(True)

        return output
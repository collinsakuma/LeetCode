class Solution:
    def AbsoluteSum(self, nums):
        output = maximum = minimum = 0

        for i in nums:
            maximum = max(maximum + i, 0)
            minimum = min(minimum + i, 0)
            output = max(output, maximum, - minimum)

        return output 
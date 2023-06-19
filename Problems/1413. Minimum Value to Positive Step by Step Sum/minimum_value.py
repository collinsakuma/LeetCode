class Solution:
    def minStartValue(self, nums):
        i, j = 0, 1
        for num in nums:
            i += num
            j = max(j, 1 - i)
        return j
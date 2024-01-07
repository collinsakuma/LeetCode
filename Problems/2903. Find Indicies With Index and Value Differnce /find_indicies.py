class Solution:
    def findIndices(self, nums, indexDifference, valueDifference):
        output = [-1, -1]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(i - j) >= indexDifference:
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        output = [i, j]
                        break
        return output
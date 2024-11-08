class Solution:
    def largestCombination(self, candidates):
        output = 0
        # find the max number of candidates that share a common bit position
        # of 1

        for i in range(32):
            count = sum(1 for candidate in candidates if candidate & (1 << i))
            output = max(output, count)

        return output
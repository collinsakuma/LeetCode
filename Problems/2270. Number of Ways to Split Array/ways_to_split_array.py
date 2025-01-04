from itertools import accumulate

class Solution:
    def waysToSplitArray(self, n):
        n = list(accumulate(n))
        return sum(n[i] >= n[-1] - n[i] for i in range(len(n) - 1))
class Solution:
    def maximumScore(self, a, b ,c):
        a, b, c = sorted((a, b, c))
        if a + b < c:
            return a + b
        else:
            return (a + b + c) // 2
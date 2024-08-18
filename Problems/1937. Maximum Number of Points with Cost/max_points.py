class Solution:
    def maxPoints(self, points):
        n, m = len(points), len(points[0])
        dp = points[0]

        left = [0] * m
        right = [0] * m

        for row in range(1, n):
            for column in range(m):
                if column == 0:
                    left[column] = dp[column]
                else:
                    left[column] = max(left[column - 1] - 1, dp[column])
            for column in range(m - 1, -1, -1):
                if column == m - 1:
                    right[column] = dp[column]
                else:
                    right[column] = max(right[column + 1] - 1, dp[column])

            for column in range(m):
                dp[column] = points[row][column] + max(left[column], right[column])
            
        return max(dp)
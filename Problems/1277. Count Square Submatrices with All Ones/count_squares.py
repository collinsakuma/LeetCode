class Solution:
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # create DP
        dp = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        # loop through range of 2D matrix
        for i in range(m):
            for j in range(n):
                # if top corner is 1
                if matrix[i][j]:
                    # check its corners in three directions return the minuim number of squares
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                    ans += dp[i+1][j+1]
        return ans
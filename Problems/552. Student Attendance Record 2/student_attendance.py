class Solution:
    def checkRecord(self, n):
        mod = 10**9 + 7
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        def recursive(i, absent, late):
            if absent >= 2 or late >= 3:
                return 0
            if i == 0:
                return 1
            if dp[i][absent][late] != -1:
                return dp[i][absent][late]
            ans = recursive(i - 1, absent, 0)
            ans += recursive(i - 1, absent, late + 1)
            ans += recursive(i - 1, absent + 1, 0)
            dp[i][absent][late] = ans % mod
            
            return dp[i][absent][late]

        return recursive(n, 0, 0)
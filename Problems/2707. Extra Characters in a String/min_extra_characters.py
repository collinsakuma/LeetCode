class Solution:
    def minExtraChar(self, s, dictionary):
        dp = [0] * 51 # initalize dp

        n = len(s)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1] # initalize with one extra character

            for w in dictionary:
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    # update if word in the dictonary is found
                    dp[i] = min(dp[i], dp[i + len(w)])

        return dp[0] # return the min extra characters in the extra string
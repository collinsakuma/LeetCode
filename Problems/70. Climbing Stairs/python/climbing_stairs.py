class Solution:
    def climbStairs(self, n):
        prev = 1
        prev2 = 0
        for i in range(1, n + 1):
            curi = prev + prev2
            prev2 = prev
            prev = curi
        return prev
    
    # second solution using dp
    def climbStairsTwo(self, n):
        # stairs of length 0 to 2 are edge cases and only one specific results
        if n <= 2:
            return n
        
        dp = [0] * (n + 1) # create the dp
        
        # set the value for the two edge cases 1 and 2 stairs
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1): # loop through range of the remaining stairs after the two edge cases
            # there are two possible steps that can be taken so add the two next step values to equal the possibel solutions for i
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n] # return the last value of the list
import math

class Solution:
    def longestIdealString(self, s, k):
        # create a list the length of the alphabet 
        dp = [0] * 26
        n = len(s)

        # loop through range of string in reverse order
        for i in range(n - 1, -1, -1):
            # set the current letter at index i
            curr_char = s[i]
            # find the index of the letter in is ascii numberic value
            index = ord(curr_char) - ord('a')
            maxi = float(-math.inf)

            # find the bounds of possible previous characters based on k value
            left = max((index - k), 0)
            right = min((index +k, 25))

            # itterate through the bounds of previous characters and find the max value of dp
            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])
                
            # update the max value of dp at the current characters index
            dp[index] = maxi + 1
        
        return max(dp)
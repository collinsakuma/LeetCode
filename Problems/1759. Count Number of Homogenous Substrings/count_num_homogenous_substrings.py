class Solution:
    def countHomogenous(self, s):
        left = 0
        output = 0

        for right in range(len(s)):
            # if characters are the same increase output by the length of the current substring
            if s[left] == s[right]:
                output += right - left + 1
            # if the letters are different increase output by 1 to account for 1 letter substring
            else:
                output += 1
                left = right # update left to start a new substring
        
        return output % (10**9 + 7)
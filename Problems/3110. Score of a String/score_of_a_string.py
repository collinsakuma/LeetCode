class Solution:
    def scoreOfString(self, s):
        total = 0
        # loop through range
        for i in range(1, len(s)):
            # add absolte difference to the total
            total += abs(ord(s[i-1]) - ord(s[i]))

        return total
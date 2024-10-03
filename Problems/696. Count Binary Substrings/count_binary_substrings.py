class Solution:
    def countBinarySubstringss(self, s):
        a, b = 0, 1 # set two pointers
        count = 0 # count of binary substrings 

        # loop through range skipping first index, beacuse it is a
        for i in range(1, len(s)):
            # if the two index match side the window
            if s[i] == s[i - 1]:
                b += 1
            # set new left side window and reset b
            else:
                a = b
                b = 1

            # incresase count of binary substrings
            if a >= b:
                count += 1

        return count
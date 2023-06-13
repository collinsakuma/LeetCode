class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        ans = -1 # set answer to -1 as default because if conditions not met return -1
        for i in range(len(s)):
            # start a loop that runs as many times as elements in s
            for j in range(i + 1, len(s)):
                # start a second loop in the range of ( i +1 ) -> the number of elements in s
                if s[i] == s[j]:
                    # the second loop will run comparing each element at s[i] to each incremented element at s[j]
                    ans = max(ans, j-i-1) 
                    # find the length between the two matching letters (hence the -1)
            return ans

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

    def maxLengthBetweenEqualCharacterTwo(self, s):
        first_dict = {} # dictionary to keep track of letter that have been iterated over already
        ans = -1 # set default answer to -1 to be returned if no matching pairs are found

        for i in range(len(s)): # loop though range of s looking for letter already in the dict, set new answer if new longer length has been found
            if s[i] in first_dict:
                ans = max(ans, i - first_dict[s[i]] - 1)
            else:
                first_dict[s[i]] = i

        return ans
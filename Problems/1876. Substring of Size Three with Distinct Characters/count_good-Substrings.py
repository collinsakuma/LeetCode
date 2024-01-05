class Solution:
    def countGoodSubstrings(self, s):
        count = 0 # keep count of substrings of length three that are made of unique characters

        for i in range(len(s) - 2): # loop though range of length of s - 2 ( the amount of substrings of length three = s - 2)
            if len(set(s[i:i + 3])) == 3: # get of a set of each substring and if its length is 3 then it is made of unique characters
                count += 1 # increase count of 3 if condition met

        return count # return count
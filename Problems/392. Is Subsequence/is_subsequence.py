class Solution:
    def isSubsequence(self, s, t):
        # set two pointer variables 
        a = 0
        b = 0
        
        while a < len(s) and b < len(t):
            if s[a] == t[b]: # if the two letters are the same
                a += 1 # move on to next letter
            b += 1 # b pointer will always move to next index regardless of if two points match
        return a == len(s) # if the whole string a is traversed return true, else return false as the subsequence was not found
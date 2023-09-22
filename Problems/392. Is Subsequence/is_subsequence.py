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
    
    def isSubsequence(self, s, t):
        index = 0

        if not s: # if s is an empty string than it is a subsequence of t
            return True
        for i in t: # loop though all letters of t
            # check if current i is the same as s[index]
            if i == s[index]: 
                # if true increment index by 1 ( next letter in s )
                index += 1
            if index == len(s): # if index is the same as length of len(s) then s is a subsequence of t
                return True
        return False # if index is not equal ot len(s) then s is not a subsequence of t return false
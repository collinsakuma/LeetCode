class Solution:
    def shortestPalindrome(self, s):
        t = s[::-1] # copy and flip the string

        # loop through range of the string
        for i in range(len(t)):
            # check at each index if the first part of s is the reducing segment of t
            if s.startswith(t[i:]):
                # if true return the reduced segment plus the whole original string
                return t[:i] + s
            
        return t + s # if no begining of the string is found, return a complete doubl flipped string
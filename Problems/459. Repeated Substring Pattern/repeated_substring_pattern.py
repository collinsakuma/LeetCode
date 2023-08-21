class Solution:
    def repeatedSubstringPattern(self, s):
        s_fold = "".join(( s[1:], s[:-1])) # fold the string into a new string where it combines the same string twice missing the first letter and missing the last letter
        return s in s_fold # if s is in s_fold then the string is being repeated
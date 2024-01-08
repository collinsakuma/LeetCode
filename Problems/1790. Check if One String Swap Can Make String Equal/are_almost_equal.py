class Solution:
    def areAlmostEqual(self, s1, s2):
        if s1 == s2: # if the two strings are already equal return True
            return True
        
        if sorted(s1) != sorted(s2): # if the two strings dont contain the same characters than the two strings cannot be made equal
            return False
        
        count = 0 # set count for differeing letters in the two strings
        for i in range(len(s1)): # loop though a range of the length of s1
            if s1[i] != s2[i]: # if the letter at index i does not match 
                # count 1 as a is math
                count += 1

        if count != 2: # if there are more than two mismatched letter the the two strings cannot be matched in one operation
            return False
        
        return True # all conditions passed return True
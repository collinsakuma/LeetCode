class Solution:
    def minLength(self, s):
        # while AB or CD are still in the string continue the loop
        while 'AB' in s or 'CD' in s:
            # loop through range of length s minus 1
            for i in range(len(s) - 1):
                # check if segment is AB or CD
                if s[i:i + 2] == 'AB' or s[i:i + 2] == 'CD':
                    # if AB or CD found remove it from the string
                    s = s[0:i] + s[i + 2:]
        
        return len(s) # return the length of the string after all instances of AB or CD have been removed
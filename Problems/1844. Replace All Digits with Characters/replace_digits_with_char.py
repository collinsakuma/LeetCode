class Solution:
    def replaceDigits(self, s):
        s = list(s) # turn the string s into a list

        for i in range(1,len(s),2): # loop though range of len(s), every second element starting at 1
            # replace the character at index i,
            # s[i-1] is the letter that comes before the number index
            # int(s[i]) is the integer value of index s[i]
            # replace s[i] with the letter value of the two added to eachother
            s[i] = chr(ord(s[i-1]) + int(s[i]))
        return "".join(s) # return a string of the new letter only s
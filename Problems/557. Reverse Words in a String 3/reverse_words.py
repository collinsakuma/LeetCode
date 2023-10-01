class Solution:
    def reverseWords(self, s):
        s = s.split(" ") # turn the string s into a list that is split where there was spaces in the string
        for i in range(len(s)): # loop though a range of length of list s
            s[i] = s[i][::-1] # at each index replace the index with a flipped version of the index
        return ' '.join(s) # rejoin the list s into a string with spaces between the indicies
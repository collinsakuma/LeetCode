class Solution:
    def toLowerCase(self, s):
        output = ""

        for i in s: # loop though letter in string s
            if 64 < ord(i) < 91: # check to ascii bit value for the letter, if letter is in the range it is upper case, convert to lowercase and add to output string
                output += chr(ord(i) + 32)
            else: # if letter is already lower case, add it to the output unmodified
                output += i
        return output
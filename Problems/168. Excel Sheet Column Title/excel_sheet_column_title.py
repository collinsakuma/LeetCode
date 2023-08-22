class Solution:
    def convertToTitle(self, columnNumber):
        output = ""

        while columnNumber > 0: # while columnNumber is greater than 0 continue to loop
            # get current character by subtracting 1 from columnNumber and taking the modulo of that from 26
            # add output to the end of the current letter
            output = chr(ord("A") + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26 # divide columnNumber by 26 

        return output
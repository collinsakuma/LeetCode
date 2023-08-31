class Solution:
    # super slopy first attempt but it works
    def compress(self, chars):
        s = ""
        curr = chars[0] # curr to compare the character currently being looked at in the loop
        count = 1 # keep track of how many times a character appears in a row

        for char in chars[1:]: # loop though chars, skipping the first index
            if curr == char: # if the both are the same letter increment count by 1
                count += 1
            elif curr != char and count == 1: # if char is a diffferent letter and it only appears once( count is 1 )
                s += curr # add onl the letter to the string
            elif curr != char and count > 1: # if char is a different letter but it appears more than once (count is greater than 1 )
                # add both the letter and how many times it appears in the string to s
                s += curr
                s += str(count)
                count = 1 # reset count to 1
            curr = char # set a new curr character
        s += curr # append the last curr to s
        if count > 1: # if its count is greater than 1 append the number of times it appears as well
            s += str(count)
        
        for i in range(len(s)): # loop through range len(s) replace the indexes in chars with the values at the same index in s
            chars[i] = s[i]

        return len(s) # return the length of s

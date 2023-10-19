class Solution:
    def restoreString(self, s, indices):
        t = [""] * len(s) # create a list equal to length t of empty strings

        for i, j in enumerate(indices): # use enumerate() to loop though indicies to keep track of the value of each index as well as the actual value
            t[j] = s[i] # set t index of j equal to s at index i

        return "".join(t) # join the list into a string and return the string
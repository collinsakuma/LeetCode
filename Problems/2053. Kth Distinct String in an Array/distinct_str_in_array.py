class Solution:
    def kthDistinct(self, arr, k ):
        output = [] # list of strings that only appear once

        for string in arr: # loop though list of strings
            if arr.count(string) == 1: # if string only appears in arr once
                output.append(string) # add that string to the output list
        
        if len(output) < k: # if the amout of unique strings in arr is less than k return an empty string
            return ""
        else:
            return output[k - 1] # minus 1 from k to account for the 0 index
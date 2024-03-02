class Solution:
    def maximumOddBinaryNumber(self, s):
        sorted_str = sorted(s, reverse=True) # sort the string in reverse order

        for i in range(len(s) - 1, -1, -1): # loop though range backwards
            if sorted_str[i] == '1': # if the element at index i is 1 swap it with the last element in the string
                sorted_str[i], sorted_str[-1] = sorted_str[-1], sorted_str[i]
                break
        
        return ''.join(sorted_str)
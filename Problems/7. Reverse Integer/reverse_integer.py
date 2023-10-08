class Solution:
    def reverse(self, x):
        str_x = str(abs(x)) # turn x into a string for reversal later, also take abs() of x to get rid of negative sign if x is negative
        new_x = 0 # set a new_x to 0

        if x < 0: # check if x is a negative number
            new_x = int(str_x[::-1]) * -1 # set new_x by reversing str_x converting it into a integer and then turing it to a negative number
        else:
            new_x = int(str_x[::-1]) # only reverse str_x and turn it into an integer
        
        # check if new_x is a 32-bit integer, if not return 0
        if new_x <= 2**31 - 1 and new_x >= -2**31:
            return new_x
        return 0
class Solution:
    def CountDigits(self, num):
        output = 0 # create an output variable to keep track of how man digits in num num is divisible by.

        for i in range(len(str(num))): # start a loop in the range of len() of num first converted into a string
            if num % int(str(num)[i]) == 0: # an int is not iterable so first convert to a string to look at the index at i
                output += 1 # if num is divisible by the int(str(num)[i]) add 1 to the output
        return output
class Solution:
    def countEven(self, num):
        output = 0 # keep track of numbers with positives sums

        for i in range(2, num + 1): # loop through range from 2 to num + 1
            sm = sum(map(int, str(i))) # sum a list of all the numbers in a converted string i
            if sm % 2 == 0: # if sm has a modulo remainder of 0 
                output +=1 # increment output by 1
        return output 
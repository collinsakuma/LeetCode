class Solution:

    # solution that I came up with should work but time complexity is too slow
    def countSpecialNumbers(self, n):

        output = 0 # variable to keep track of count of special numbers

        for i in range(1, n + 1): # loop though range of 1 - n
            flag = True # set flag variable to True (is special number)
            for num in str(i): # loop though the digits of the number
                if str(i).count(num) != 1: # if num only has a .count() of each digit of anything except 1 then it is not a special number
                    flag = False # i is not a special number so set flag as False
            
            if flag: # if the flag remains true add 1 to output becuase i is a speical number if flag equal False do no increase output by 1 becuase i was not a speical number
                output += 1 

        return output 
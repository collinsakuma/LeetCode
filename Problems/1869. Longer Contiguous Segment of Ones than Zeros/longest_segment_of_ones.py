class Solution:
    def checkZeroOnes(self, s):
        max_one = 0 # variable to keep track of longest streak of consecutive ones
        max_zero = 0 # variable to keep track of longest streak of consecutive zeros
        streak_one = 0 # current count of consecutive ones
        streak_zero = 0 # current count of consecutive zeros

        for i in s: # loop though each number in s
            if int(i) == 1: # check if i is 1
                streak_zero = 0 # if i is one set current streak_zero to 0
                streak_one += 1 # increment current streak of ones by 1
                if streak_one > max_one: #if the current streak of ones is greater than max_one set the current streak as the max streak reached so far
                    max_one = streak_one
            else: # if i is 0
                streak_one = 0 # zero out the current streak of ones (if any)
                streak_zero += 1 # increment current streak of zeros by 1
                if streak_zero > max_zero: # if current streak of 0s is greater than streak of zeros achieved so far set new max_zero val
                    max_zero = streak_zero 
        if max_one > max_zero: # if there was a long streak of ones than zeros return True else False
            return True
        else:
            return False
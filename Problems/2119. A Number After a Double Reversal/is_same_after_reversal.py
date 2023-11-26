class Solution:
    def isSameAfterReversals(self, num):
        if num == 0: # special case, 0 reversed is the same
            return True
        num = str(num) # turn the number into a string

        if num[-1] == "0": # check if the last digit in the number is 0, if there is a 0 when reversed the number will not be the same
            return False
        return True
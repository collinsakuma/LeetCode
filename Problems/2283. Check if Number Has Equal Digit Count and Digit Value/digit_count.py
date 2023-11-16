class Solution:
    def digitCount(self, num):
        for index, number in enumerate(num): # loop through each element in num, number, keeping track of the elements index as well
            # check if the count of index in num is not equal to the number
            if num.count(str(index)) != int(number):
                # if not equal then condition for string have not been meet return False
                return False
        return True # if all numbers and index pass the check return True
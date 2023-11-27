class Solution:
    def numDifferentIntegers(self, word):
        nums = [] # list to keep numbers in
        number = "" # keep track of numbers between letters
        for i in word: # loop though each element in string
            if i.isdigit(): # check if i is a number if so build the number
                number += i
            else: # if i is a letter then if there is numbers in number currently add that number to the list of numbers
                if number:
                    nums.append(int(number))
                    number = "" # reset number to an empty string
        if number: # after loop is completed check if there is a number at the end of the string if so append that number to the list
            nums.append(int(number))

        return len(set(nums)) # return the length of unique numbers in the list
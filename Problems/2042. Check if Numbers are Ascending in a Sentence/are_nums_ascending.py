class Solution:
    def areNumbersAscending(self, s):
        assending = [] # keep a list of the numbers in s
        s_list = s.split(" ") # separeate the string s into a list separeted by spaces

        for i in s_list: # loop though the list of strings
            if i.isdigit(): # check if each string is a number
                assending.append(int(i)) # if the string is a number, convert it to an int and add it to the list

        # check if the build list of numbers, is equal to a set of sorted list 
        # if list are the same then numbers in s are assending True is returned
        return assending == sorted(set(assending))
class Solution:
    def maximunValue(self, strs):
        maximum = 0 # create a maximum value to keep track of the max value of strings

        for item in strs:
            if item.isdigit(): # .isdigit() method checks if all characters are digits in a string
                maximum = max(maximum, int(item)) # take the max( the current max, or the item converted to a integer)
            else:
                maximum = max(maximum, len(item)) # take the max( the current max, of the lenght of the item string)
        return maximum # return the maximum variable after all items in strs have been looped through
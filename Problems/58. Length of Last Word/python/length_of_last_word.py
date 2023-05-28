class Solution:
    def lengthOfLastWord(self, s):
        split_string = s.split()
        # split the string into a list between the spaces of the words
        return len(split_string[-1])
        # return the length of the last element in the list
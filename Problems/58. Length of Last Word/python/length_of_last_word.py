class Solution:
    def lengthOfLastWord(self, s):
        split_string = s.split()
        # split the string into a list between the spaces of the words
        return len(split_string[-1])
        # return the length of the last element in the list
    
    # solution 4/1/24
    def lengthOfLastWordTwo(self, s):
        s = s.split() # split the string 
        while s: # while there are elements in s
            word = s.pop() # pop the last element from the list s
            if word:
                return len(word) # return the length of the word
            

    # iteration of second solution cleaned up but same general method
    def lengthOfLastWordThree(self, s):
        s = s.split()
        return len(s.pop())

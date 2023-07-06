class Solution:
    def countWords(self, words1, words2):
        output = 0 # create a variable to keep track of words that occur once in both list
        for word in words1: # loop though all of the words in the first list
            if words1.count(word) == 1 and words2.count(word) == 1: # count the number of times that word appears in both list 1 and 2
                output += 1 # if true increase th output by 1
        return output # return the number of words that occur in each list once
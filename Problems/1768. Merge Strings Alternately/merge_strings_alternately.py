class Solution:
    def mergeAlternately(self, word1, word2):
        output = ""
        # convert both words into lists
        word1 = list(word1)
        word2 = list(word2)

        while word1 or word2: # while word1 and word2 have elements
            if word1: # if word1 still has elements
                output += word1.pop(0) # pop first element from word1 and add it to output
            if word2: # if word2 still has elements
                output += word2.pop(0) # pop first element from word2 and add it to output
        return output
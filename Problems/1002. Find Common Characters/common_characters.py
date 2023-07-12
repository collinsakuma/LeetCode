class Solution:
    def commonChars(self, words):
        common = [] # create empty list to hold common letters
        word1 = set(words[0]) # create a set of unique letters in the first word

        for char in word1: # loop though the set of letters
            frequency = min([word.count(char) for word in words]) # find the minimum frequency of how many times each letter occurs in all words
            # if the char does not appear in one of the words 0 will be set as the frequency beacuse if gets the min of all words. 
            common += [char] * frequency # add the letter to the common list * the amount of times the letter appears in all words

        return common 
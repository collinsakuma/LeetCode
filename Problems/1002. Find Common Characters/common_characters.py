class Solution:
    def commonChars(self, words):
        common = [] # create empty list to hold common letters
        word1 = set(words[0]) # create a set of unique letters in the first word

        for char in word1: # loop though the set of letters
            frequency = min([word.count(char) for word in words]) # find the minimum frequency of how many times each letter occurs in all words
            # if the char does not appear in one of the words 0 will be set as the frequency beacuse if gets the min of all words. 
            common += [char] * frequency # add the letter to the common list * the amount of times the letter appears in all words

        return common 
    
    def commonCharsTwo(self, words):
        # set array to hold common characters
        common_characters = []

        # loop through a set of letters in the first word
        for letter in set(words[0]):
            # set a count of the # of occurances of letter in the first word
            count = words[0].count(letter)

            # loop through the rest of the words in words
            for word in words[1:]:
                # find the minimum count of letter in words
                count = min(word.count(letter), count)
            # if letter is a common character among all words add it to the list of common characters
            common_characters += [letter] * count 

        return common_characters
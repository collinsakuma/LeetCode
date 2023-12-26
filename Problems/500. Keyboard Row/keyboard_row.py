class Solution:
    def findWords(self, words):

        # create dictionaries of the letter in each row of a keyboard
        row1 = {'q','w','e','r','t','y','u','i','o','p'}
        row2 = {'a','s','d','f','g','h','j','k','l'}
        row3 = {'z','x','c','v','b','n','m'}

        output = [] # create an empty list to hold words that can be typed using one row.

        for word in words:
            wordset = set(word.lower()) # create a set of all the letters in each word( excludes duplicate letters)
            if (wordset & row1 == wordset) or (wordset & row2 == wordset) or (wordset & row3 == wordset):
                output.append(word)
        return output

class Solution:
    def makeEqual(self, words):
        joined_words = ''.join(words) # join all the words in the list into a single string
        letter_set = set(joined_words) # create a set of unique letter from joined_words

        for letter in letter_set: # iterate through the set of letters
            if joined_words.count(letter) % len(words) != 0:
                # check the count of the letter in string of the joined list
                # the count of letters should be equal to the length of the words list returing a modulo of 0
                return False # if 0 is not the remainder then equal strings cannot be made and return 0
        return True
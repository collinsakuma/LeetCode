class Solution:
    def reorderSpaces(self, text):
        word_list = text.split() # split text into a list of words
        spaces = text.count(" ") # count the amount of spaces that appear in the string
        word_count = len(word_list) # count how many words are in the string

        if word_count == 1: # if text string is only one word return the single word with all spaces added at the end of the string
            return (word_list[0] + " " * spaces)
        else:
            # use divmod() to track quotient and remainder as variables q and r
            q, r = divmod(spaces, word_count - 1)
            # join the wordlist, with q number of spaces between, (the quotent) and remainder of spaces r at the end of the string
            return ( (" " * q).join(word_list) + " " * r)
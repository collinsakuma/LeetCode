class Solution:
    def isAcronym(self, words, s):
        acronym = "" # build the acronym of words
        for word in words: # loop through each word in words and add to the acroym
            acronym += word[0]

        return acronym == s # compare the two acronyms return true if they match, false if they do not
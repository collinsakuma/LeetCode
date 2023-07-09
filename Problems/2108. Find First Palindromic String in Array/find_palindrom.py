class Solution:
    def firstPalindrome(self, words):
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                # for each word in the list check if it is the same as the reversed of the word
                # if palandromic return that word
                return words[i]
        return ''
        # if no words are palandromic return an empty string

    def firstPalindromeTwo(self, words): # solution from 7/9/23
        for word in words: # loop though words list instead of loop though range of len(words) much cleaner this way
            if word == word[::-1]: # check if word == to backwards version of word if true than word is a palindrom
                return word
        return "" # return empty string if no word in words is a palindrom
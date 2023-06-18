class Solution:
    def firstPalindrome(self, words):
        for i in range(len(words)):
            if words[i] == words[i][::-1]:
                # for each word in the list check if it is the same as the reversed of the word
                # if palandromic return that word
                return words[i]
        return ''
        # if no words are palandromic return an empty string
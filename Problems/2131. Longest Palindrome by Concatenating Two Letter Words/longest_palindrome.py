from collections import Counter

class Solution:
    def longestPalindrome(self, words):
        # pairs to keep track of 2 pairs found
        # sym to keep track of symetrical words not in pairs
        # not_paired is the Counter() dict
        pairs, sym, not_paired = 0, 0, Counter()

        for word in words: # loop through words
            # if there is a match of the reverse of word in not_paired
            if not_paired[word[::-1]] > 0:
                pairs += 1 # increase the count of pairs by 1
                not_paired[word[::-1]] -= 1 # decrease the value count for word[::-1] by 1 as its already paired up
                if word[0] == word[1]: # if the word is symetrical I.E. "aa" or "xx"
                    sym -= 1 # reduce the count of symetrical non paired words by 1
            else: # if word has no matching reverse word
                not_paired[word] += 1 # increase the count of word in not_paired
                if word[0] == word[1]: # if the word is symetrical
                    sym += 1 # increase symetrical count by 1
        
        # pairs are sized in 4 ( "ab" * "ba" ) have length 4
        # if there is a symetrical word not in use add it to the middle of the palindrome ( + 2 )
        return pairs * 4 + (2 if sym > 0 else 0)
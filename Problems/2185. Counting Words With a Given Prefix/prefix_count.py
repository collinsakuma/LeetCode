class Solution:
    def prefixCount(self, words, pref):
        output = 0

        for word in words: # loop through words list
            # only check the first part of word that is equal to the length of the given prefix
            if word[:len(pref)] == pref:
                # if the prefix matches the substring of word increase output by 1
                output += 1
        return output
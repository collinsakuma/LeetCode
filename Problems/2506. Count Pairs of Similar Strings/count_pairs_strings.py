class Solution:
    def similarPairs(self, words):
        count = 0 # set count variable to keep track of words with same characters
        for i in range(len(words)): # loop though range of the length of words list
            for j in range(i): # second loop for range of what i is being looped
                if set(words[i]) == set(words[j]): # use set() to check a set of unique charaters in each word and compare it to the next index j
                    count += 1 # if the set() is the same increment count by 1
        return count
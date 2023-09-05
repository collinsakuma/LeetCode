class Solution:
    def maxVowels(self, s, k):
        vowels = "aeiou" # string of all vowels
        max_vowels = curr_vowels = 0 # set max and curr vowel counts

        for i in range(len(s)): # loop though range of len s
            # if i is greater than k then check the index leaving the "window"
            # also before we can check if indexes exiting the window are vowels you first need to check the staring k number of indexes that wont have any outgoing indexes
            if i >= k:
                if s[i - k] in vowels: # if the index exiting the window was a vowel then reduce the curr_vowels count by 1
                    curr_vowels -= 1
            # if curr index i is a vowel then increase the curr_vowels count by 1
            if s[i] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels) # for each loop check if curr_vowels is greater than max_vowels if so set new max_vowels

        return max_vowels
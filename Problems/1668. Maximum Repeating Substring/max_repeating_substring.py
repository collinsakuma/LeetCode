class Solution:
    def maxRepeating(self, sequence, word):
        # k_repeating tracks count of word repeating in sequence
        # original_word is a copy of the substring word 
        k_repeating, original_word = 0, word

        # while word is in the sequence
        while word in sequence:
            # incrase count of k
            k_repeating += 1
            # concadenate one iteration of the original substring word
            word = word + original_word

        # return the amount of times the substring (word) appears in sequence consecutively
        return k_repeating
    

    # second solution more clean code wise
    # run time is slower however??? 
    # - runtime difference may be down to how string concatenation is handled line 25
    # - leetcode gave a faster run time when replaceing line 25 with 
    #   k_repeating_word = k_repeating_word + word
    def maxRepeatingtwo(self, sequence, word):
        k_repeating_word = word

        while k_repeating_word in sequence:
            k_repeating_word += word
        
        return len(k_repeating_word) // len(word) - 1

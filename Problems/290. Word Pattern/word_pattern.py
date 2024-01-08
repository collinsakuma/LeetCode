class Solution:
    def wordPattern(self, pattern, s):
        dict = {} # dictionary to keep track of letter and the word that it goes with
        s = s.split(" ") # split s into a array of words

        # must be a 1 to 1 ratio of pattern lenght to words
        if len(s) != len(pattern): 
            return False

        # there must be an equal amount of each set of s and pattern
        if len(set(s)) != len(set(pattern)):
            return False
        
        for i in range(len(pattern)): # loop though range of length pattern
            if pattern[i] in dict: # if the pattern letter is in the dict
                # check that the corresponding word is the same as the current s[i] word
                if dict[pattern[i]] != s[i]:
                    return False # if not the pattern is not consistent return False
            else: # if letter is not already in dict, create a new entry with letter as key and word as value
                dict[pattern[i]] = s[i]
        
        return True # if all letters in patter have been looped though and pass conditions return True
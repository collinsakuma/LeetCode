class Solution:
    def rearrangeCharacters(self, s, target):
        
        char_set = set(target) # create a set of all the letters in the target string
        output = 10000 # set an arbitary output number that will be replaced (must be high)

        for char in char_set: # loop though the characters in the char_set
            if output > s.count(char) // target.count(char):
                output = s.count(char) // target.count(char)
                # check the .count() of char in string s divided by the .count() of char in target
                # this will give you the amount of times the target word can be created with s letters.
                # return the char that can create the LEAST amount of instances of the target word.
        return output
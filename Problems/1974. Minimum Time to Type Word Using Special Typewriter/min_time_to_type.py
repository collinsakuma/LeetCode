class Solution:
    def minTimeToType(self, word):
        output = len(word)
        prev ="a" # type write starts at position a
        for ch in word: # loop through characters in the string
            val = (ord(ch) - ord(prev)) % 26 # amount of spaces that the typewriter needs to move to get to the next character
            output += min(val, 26 - val) # determine if it is faster to travers to the next ch by going left or right on the typewriter wheel
            prev = ch # set a new prev character to the one in this loop

        return output # return the amount of time it takes to type the word
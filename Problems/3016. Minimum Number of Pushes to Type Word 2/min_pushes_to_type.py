from collections import Counter

class Solution:
    def minimumPushes(self, word):
        output = 0 # count of minimum button presses
        count = Counter(word) # create a dict to track the frequency of each character in word
        # sort the count dict by the values in descending order
        count = sorted(count.items(), key=lambda x:x[1], reverse=True)

        # loop through count tracking the index of each (character, character frequency)
        for index, (ch, freq) in enumerate(count):
            # - check if the index can be the first letter on any of the given 8 keys
            #   if the index is over 8 then it must be on a secondary key, over 16 third key stroke....etc
            # - multiply the frequency of the character by the depth of the key that it will be on
            output += freq * ((index // 8) + 1)
        
        return output
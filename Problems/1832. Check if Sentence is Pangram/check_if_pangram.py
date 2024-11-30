from collections import Counter

class Solution:
    def checkIfPangram(self, sentence):
        # use Counter() to create a dict of all the letter that are used
        count = Counter(sentence)

        # check if length of the count is 26 long if so every letter
        # in the alphabet is used
        if len(count) == 26: return True
        else: return False

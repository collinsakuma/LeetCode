from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        # set window of length of stirng s1
        window = len(s1)
        # create a counter of s1
        s1_counter = Counter(s1)

# loop through range of s2 minus the lenght of s1 to check for possible permuations
        for i in range(len(s2) - window + 1):
            # create a counter in the window of s2
            s2_counter = Counter(s2[i:i + window])
            # if the two counters are equal then a permuation exist
            if s2_counter == s1_counter:
                return True

        # return false if no permutations found
        return False
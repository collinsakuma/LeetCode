class Solution:
    def minChanges(self, s):
        changes = 0

        # loop through range of string, in increments of 2
        for i in range(0, len(s) - 1, 2):
            # if pairs are the same continue
            if s[i] == s[i + 1]:
                continue
            # one number needs to be flipped add a change
            else:
                changes += 1

        return changes # return min number of changes 
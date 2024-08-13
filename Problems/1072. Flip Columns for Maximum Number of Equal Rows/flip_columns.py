from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        pattern = defaultdict(int)

        # loop through rows in matrix
        for row in matrix:
            # add the pattern to the dict of patterns with a value of 1
            pattern[tuple(row)] += 1
            # flip the pattern 
            flip = [1 - c for c in row]
            # add the flipped pattern to the dict of patterns
            pattern[tuple(flip)] += 1

        # return the max value of the pattern with the greatest reaccurance
        return max(pattern.values())
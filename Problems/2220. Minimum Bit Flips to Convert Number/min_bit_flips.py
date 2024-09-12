class Solution:
    def minBitFlips(self, start, goal):
        # convert to bit
        output = start ^ goal
        count = 0

        # while output
        while output:
            # use the & operator to check for mis matched bits
            output &= output - 1
            count += 1
        return count
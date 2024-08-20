class Solution:
    def minSteps(self, n):
        if n == 1:
            return 0
        # track operations made
        steps = 0 
        # start with a factor of 2 as the lowest possible factor
        factor = 2

        # while there are still 'A's to get print continue the loop
        while n > 1:
            # divide n by the factor as much as possible
            while n % factor == 0:
                # if you can divide by the factor add (factor) number of steps
                steps += factor
                # reduce n by the factor
                n //= factor 
            # if n no longer has a factor of factor increment the factor
            factor += 1

        return steps # return steps taken
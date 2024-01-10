class Solution:
    def distributeCandies(self, n, limit):
        count = 0 # keep track number of ways candies can be distributed

        # start three for loops each one representing one of the three children
        # loop in the range of limit + 1 ( plus 1 to account for 0 index )
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    # if the combined total of distributed candies equal the number of candies than a distribution has been found
                    if i + k + j == n:
                        count += 1 # increase count by 1

        return count
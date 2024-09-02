class Solution:
    def construct2DArray(self, original, m, n):
        two_d_list = []

        # if there are not enough element to construct such a 2d array return False
        if len(original) != m * n:
            return []

        # loop through range of the length of the 1D array
        # loop in an interval equal to n
        for i in range(0, len(original), n):
            # append arrays to the matrix from index i to index i + n
            two_d_list.append(original[i:i+n])

        return two_d_list # return the 2D array
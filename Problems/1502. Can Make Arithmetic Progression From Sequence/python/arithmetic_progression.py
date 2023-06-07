class Solution:
    def canMakeArithmeticProgression(self, arr):
        sorted_array = sorted(arr)  # first sort the arr in order.
        diff = sorted_array[0] - sorted_array[1] # calculate the differene between the first two indexes( all subsequent indexes must have same diff)
        for i in range(1, len(sorted_array) - 1):
            # loop through in the range from 1 to the length of sotred_array - 1(to account for 0 index)
            if sorted_array[i] - sorted_array[i + 1] != diff:
            # compare the difference between the points in the array and see if the diff is the same as the variable diff
                return False
                # if the diff is not equal then the a arithmetic progression sequence is not true
        return True
        # if all calculated differences are == to the diff variable then is it a arithmetic progression sequence and true is returned. 
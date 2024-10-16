class Solution:
    def minimumSteps(self, s):
        output = 0 # number of swaps needed
        count_0 = 0 # count of zeros encountered

        # loop through range right to left
        for i in range(len(s) - 1, -1, -1):
            # count the number of 0's encountered
            if s[i] == '0': count_0 += 1
            # when a 1 is encountered, add to the output the number of 0's already encountered
            else: output += count_0

        return output # return min steps
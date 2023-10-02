class Solution:
    def winnerOfGame(self, colors):
        a = b = 0 # set initial values of a and b to zero, keep track of how many "AAA" and "BBB" are in colors

        for i in range(1, len(colors) - 1): # loop through range of colors skipping first and last index
            if colors[i - 1] == colors[i] == colors[i + 1]: # check if indicies to the left and right of i are the same letter "A" or "B"
                if colors[i] == "A": # if all three letters are the same check what letter combo it is
                    # if "A" increment a by 1
                    a += 1
                else:
                    # if "B" increment b by 1
                    b += 1
        return a > b # if more A's can be removed Alice wins return True, else Return False because Bob will win
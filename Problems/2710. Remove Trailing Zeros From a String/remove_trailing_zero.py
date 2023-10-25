class Solution:
    def removeTrailingZeros(self, num):
        num = list(num) # turn num string into a list
        # loop though range of lenghh nums in reverse order
        for i in range(len(num) - 1, -1, -1):
            if num[i] == "0": # if num at index i is a 0 pop that index
                num.pop(i)
            else:
                break # if i is not a 0 then no more trailing 0's exist
        return "".join(num) # join string
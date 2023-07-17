class Solution:
    def minSwaps(self, s):
        open_bracket = 0 # keep track of the amount of open brackets there are
        # because the number of open and closed brackets are the same, its only necessary to keep track of one.

        for c in s: # loop though string
            if open_bracket > 0 and c == "]": 
                open_bracket -= 1
            elif c == "[":
                open_bracket += 1
        return (open_bracket + 1) // 2 # (open_bracket + 1) is to account for cases where there are odd number of bracket pairs resulting in the need for on additional operation
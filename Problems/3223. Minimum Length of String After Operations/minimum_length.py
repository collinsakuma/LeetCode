from collections import Counter

class Solution:
    def minimumLength(self, s):
        # create a count of letter in s
        count = Counter(s)
        output = 0

        # loop through count of letters
        for (_, num) in count.items():
            # if there are more than 2 of the same letter and the count is divisible by 2
            # add 2 to output lenght
            if num >= 2 and num % 2 == 0:
                output += 2
            # if there are 3 or more and a odd count add 1
            elif num > 2 and num % 2 == 1:
                output += 1
            else: # else add the full count to the output
                output += num

        return output 
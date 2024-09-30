from collections import Counter

class Solution:
    def minimumPushes(self, word):
        # count of the number of pushes to type out word
        min_pushes = 0
        # create a Counter() of word
        count = Counter(word)
        # sort the dic by the count of each letter in reverse order, (descending)
        count = sorted(count, key=lambda x:x[1], reverse=True)

        num_buttons = 0 # number of buttons used

        # loop through each character in the counter that needs to be typed out:
        # - ch = character
        # - ct = the count of the character in word
        for ch, ct in count:
            # add the number of pushes needed to add each instance of that letter
            # divide the num buttons by 8 to see if you need an additonal push per character
            min_pushes += ct * ((num_buttons // 8) + 1)
            # increase the number of buttons used by 1
            num_buttons += 1

        return min_pushes # return the minumum pushes necessary to type word
class Solution:
    def addSpaces(self, s, spaces):
        new_s = '' # build new string with spaces
        curr_s = 0 # index of the last letter added from s

        # while spaces need to be added
        while spaces:
            # pop the first space input index
            space = spaces.pop(0)
            # if the space is before the current index add the space to the new string
            if space <= curr_s:
                new_s += ' '
            # add letters from x up to the space
            else:
                new_s += s[curr_s:space]
                # add the space
                new_s += ' '
                # set the new current index to the index of the space
                curr_s = space
        
        # if there is left over letters after the space add the rest of the letters from s
        if curr_s < len(s):
            new_s += s[curr_s:]

        return new_s
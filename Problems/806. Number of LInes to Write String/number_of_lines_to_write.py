class Solution:
    def numberOfLines(self, widths, s):
        # set curr_line to keep track of width of the current line of letters
        # set lines to keep track of total lines used
        curr_line, lines = 0, 0 
        for i in s: # loop though all letters in string s
            # check if curr_line plus the width of the next letter is less than of equal to 100 width
            if curr_line + widths[ord(i) - 97] <= 100:
                curr_line += widths[ord(i) - 97] # if new letter does not put the current line over the 100 width limit add its width to the curr_line variable
            else: # if width of the next letter will put curr_line over the 100 width limit start a new line
                lines += 1 # increase the line count by 1, as a new line must be started
                curr_line = widths[ord(i) - 97] # set the new line width to the width of current letter i
        
        # return the two values as an array, increase line count by 1 to account for the line of curr_line
        return [lines + 1, curr_line] 
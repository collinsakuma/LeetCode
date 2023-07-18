class Solution:
    def minInsertions(self, s):
        s = s.replace("))", "}")  # replace all instances of "))" with "}" to see which closing brackets need to be closed and how many closing bracket pairs we already have
        missing_brackets = 0 # variable to keep track of how many brackets are missing
        required_closing = 0 # variable to keep track of how many closing brackets are missing

        for bracket in s: # loop though string s
            if bracket == "(": # if the bracket is an opening bracket 
                required_closing += 2 # add 2 to required_closing becuase an opeing bracket needs a correspoinding pair of closing brackets
            
            else:
                if bracket == ")": # if bracket is a closing bracket it needs its corresponding pair
                    missing_brackets += 1 # add one to missing brackets
                
                if required_closing: # if required closing is not 0 then minus 2 because if the bracket is ")" then only additional parenthesis is needed and that is being added by missing_brackets += 1 on line 13
                    # also if the current bracket is } than that is equivalent to )) meaning that if required_closing is not 0 it can be reduced by 2 because a closing bracket exist
                    required_closing -= 2
                
                else: # last case of an unmatched ) or )) needing to insert a ( to balance the string
                    missing_brackets += 1 

        return missing_brackets + required_closing
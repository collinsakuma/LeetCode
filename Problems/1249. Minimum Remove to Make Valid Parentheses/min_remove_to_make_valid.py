class Solution:
    def minRemoveToMakeValid(self,s):
        s = list(s)
        stack = []

        # loop through s
        for i, letter in enumerate(s):
            # if a left parentheses append it to the stack
            if letter == '(':
                stack.append(i)
            elif letter == ')':
                # if right parentheses and there are left parentheses pop its pair from the stack
                if stack:
                    stack.pop()
                else: # else remove the parentheses from the string
                    s[i] = ''

        while stack: # while unpaired parentheses in string replace those indexes with empty string
            s[stack.pop()] = ''
        
        return ''.join(s) # rejoin list into string
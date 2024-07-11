class Solution:
    def reverseParentheses(self, s):
        stack = []
        output = ''

        # loop through characters in the string
        for ch in s:
            # if character is a opening parentheses
            if ch == '(':
                # append the current output string to the stack
                stack.append(output)
                # set output string to an empty string
                output = ''
            # if character is a closing parentheses
            elif ch == ')':
                # reverse the current output string
                output = output[::-1]
                # pop the the last string from the stack and add the reverse string to the end of it
                output = stack.pop() + output
            # if character is not a parentheses add the letter to the current output string
            else:
                output += ch
        return output
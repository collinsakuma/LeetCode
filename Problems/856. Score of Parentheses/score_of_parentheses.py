class Solution:
    def scoreOfParentheses(self, s):
        # set a stack to keep track of value of parentheses
        stack = [0]

        for char in s: # loop though each parentheses in s
            if char == "(": # if char is a left parentheses append a new starting (parent) parentheses
                stack.append(0)
            else: # if a closing parentheses
                # set a value variable to max of either:
                # 2 times the last variable in the stack or if the last variable is 0 set value to 1
                value = max(2 * stack.pop(), 1)
                stack[-1] += value # add value to the last index of the stack
        
        return stack.pop() # return the last variable of stack
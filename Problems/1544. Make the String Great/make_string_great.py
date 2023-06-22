class Solution:
    def makeGood(self, s):
        
        stack = [] # create a stack 

        for i in range(len(s)):
            if stack and stack[-1] == s[i].swapcase():
                # check if the stack isnt empty & if the last element of the stack is = to s at index i
                stack.pop() # if both conditions are met .pop() the last element from the stack
            else:
                stack.append(s[i]) # if one of the conditions is not met append the element at index i to the stack
        return ''.join(stack) # join the array into a string and return said string of letters
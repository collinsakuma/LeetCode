class Solution:
    def makeFancyString(self, s):

        stack = [] # create a stack 

        for i in s: # loop through each letter in the string s
            if len(stack) > 1 and stack[-1] == stack[-2] == i:
                # make sure both conditions are met:
                # - 1st that the stacks length is greater than 1 because you need at least two elements to check 
                # - 2nd check if the last and second to last index of the stack are the same letter as i
                # - if both conditions are met .pop() the last element from the stack
                stack.pop()
            stack.append(i) # append i to the stack.
        return ''.join(stack) # join the stack into a string and return said string
    
    # second solution 11/1/2024
    def makeFancyStringTwo(self, s):
        fancy_s = '' # string to hold fancy string
        for ch in s: # loop through characters in s
            # if the string does not have 2 characters in it yet add the characters
            if len(fancy_s) < 2:
                fancy_s += ch
            # check for three consecutive characters if three in a row skip character
            elif ch == fancy_s[-1] == fancy_s[-2]:
                continue
            # add the character 
            else:
                fancy_s += ch
        return fancy_s
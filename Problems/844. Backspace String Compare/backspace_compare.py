class Solution:
    def backspaceCompare(self, s, t):
        # create two stacks one for sting s and one for string t
        stack_s = []
        stack_t = []

        # loop though each value in string s
        for i in s:
            if i != "#": # if element does not equal a "#" add the value to the stack
                stack_s.append(i)
            elif not stack_s: # if the value is a "#" but there are no elements in stack_s do nothing
                None
            else: # if a "#" is the current element and the stack has values in it .pop() the last value in stack_s
                stack_s.pop()

        for j in t:
            if j != "#":
                stack_t.append(j)
            elif not stack_t:
                None
            else:
                stack_s.pop()

        return stack_s == stack_t # return True if stack_s and stack_t are equal
class Solution:
    def removeDuplicates(self, s):
        stack = [s[0]] # initialize a new stack
        for i in range(1, len(s)):
            if(stack and stack[-1] == s[i]):
                # check the elements in the stack if the stack exist & the last element in the stack
                # equals s[i] then pop the last element in the stack
                stack.pop()
            else: stack.append(s[i])
        return "".join(stack)
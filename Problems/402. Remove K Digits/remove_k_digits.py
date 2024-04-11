class Solution:
    def removeKdigits(self, num, k):
        # create an empty stack
        stack = []

        for i in num:
            # while there are numbers still in the stack, there are still k numbers to remove, and the last element in the stack is greater than 0
            while stack and k and stack[-1] > 0:
                stack.pop()
                k -= 1

            # if there are elements in the stack and the current element is not 0
            # append the element to the stack
            if stack or i is not '0':
                stack.append(i)

        # if after all elements in num have been looped though and there are still k elements to remove, remove the elements from the end of the stack
        if k:
            stack = stack[0:-k]

        # join the stack into a string or if there is no stack return '0
        return ''.join(stack) or '0'
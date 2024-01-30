class Solution:
    def evalRPN(self, tokens):
        
        # update helper function
        def update(sign):
            # set the two last elements in the stack to variables n1 and n2
            n2, n1 = stack.pop(), stack.pop()
            # if the sign in an operation perform the operation on n1 and n2 and return the value
            if sign == "+": return n1 + n2
            if sign == "-": return n1 - n2
            if sign == "*": return n1 * n2
            if sign == "/": return int(n1 / n2)

        stack = [] # set an empty stack 

        for i in tokens: # loop though the list
            if i.isdigit() or len(i) > 1: # if i is a number append it to the stack, turing the string to an integer
                stack.append(int(i))
            else: # if i is not a number then it is an operation, append the result after the operation is completed
                stack.append(update(i))

        return stack.pop()
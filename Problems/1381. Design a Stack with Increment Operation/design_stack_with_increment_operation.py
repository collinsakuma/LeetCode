class CustomStack:

    def __init__(self, maxSize):
        self.stack = [] # initalize the stack as an empty list
        self.maxSize = maxSize # initalize a variable maxSize that represents the max length the stack is allowed to be

    def push(self, x):
        # if the stack is under the maximum allowed length then add x to the stack
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        # if the stack has elements in it, pop the last element in the list and return it
        if self.stack:
            return self.stack.pop()
        return -1 # if stack is empty return -1
    
    def increment(self, k, val):
        # if the stack is greater than or equal to k in length
        if len(self.stack) >= k:
            # loop through range of k and increment each element by val
            for i in range(k):
                self.stack[i] += val
        else: # if stack is length less than k, loop through the stack
            for j in range(len(self.stack)):
                self.stack[j] += val # increment each element in the stack by val
class MyQueue:
    def __int__(self):
        self.queue = [] # initalize the class with a queue as a list

    def push(self, x):
        self.queue.append(x) # for a push operation append x to the queue list

    def pop(self):
        if self.queue: # if there are values in the queue, remove the value at the front of the queue and return it
            return self.queue.pop(0)
    
    def peek(self):
        if self.queue: # only return the value of the first element of the queue, do not manipulate the queue in anny way
            return self.queue[0]
        
    def empty(self):
        if self.queue: # if the queue has elements in it return False
            return False
        return True # if the queue is empty return True
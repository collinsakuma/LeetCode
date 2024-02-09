class PeekingIterator:
    def __int__(self, iterator):
        # initalize class with the iterator
        self.iterator = iterator
        # set curr value to be the next / first value in the iterator, check if there is a next value, if not return None
        self.curr = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        # curr values represents the next value if chosen return it
        return self.curr
    
    def next(self):
        value = self.curr # set value to the curr
        # increment self.curr to the next value if there is not next return None
        self.curr = self.iterator.next() if self.iterator.hasNext() else None

    def hasNext(self):
        # if self.curr does not equal None then there is a next value after the current one
        return self.curr != None
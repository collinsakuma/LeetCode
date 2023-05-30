class MyHashSet:
    
    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size
        # table will be used to store the values

    def create_hash_value(self, key):
        # function takes a key as an input and return the hashed value of that key
        return key % self.size

    def add(self, key):
        hash_value = self.create_hash_value(key)  # creates the hash value of the key. 

        if self.table[hash_value] == None:
            # checks the value at the hashed index, if there is None then there are no values stored at that index.  
            self.table[hash_value] = [key]
            # if None a new list is created at that index with the key as the only element. 
        else: 
            self.table[hash_value].append(key)
            # if there are values at that index already the key is appened to the existing list. 

    def remove(self, key):
        hash_value = self.create_hash_value(key)

        if self.table[hash_value] != None:
            # If the value at the index of the hashed key is NOT None then there are value(s) at that index. 
            while key in self.table[hash_value]:
                # while the value of key is in the list of elements in that list at the index of table[hash_value] the loop with continue to run.
                self.table[hash_value].remove(key)
                # remove the element that matches the value of key from the self.table[hash_value] list.

    def contains(self, key):
        hash_value = self.create_hash_value(key)

        if self.table[hash_value] != None:
            # if the value at the index of the hashed key is not None then there is a list of values there.
            return key in self.table[hash_value]
            # in the list of values at self.table[hash_value] check if any of the elements in the list are equal to the value of key. If True return True.
        return False
        # if the list of values does not have the value of key present return False as the hashset does not contain the key. 
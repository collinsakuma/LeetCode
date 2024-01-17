import random
class Solution:
    def __init__(self):
        # maintain a list and a dictionary to keep track of elements and their index in the list
        self.data_map = {} 
        self.data = []

    def insert(self, val):
        
        # if the item ( val ) is already in the data set we are instructed to return False
        if val in self.data_map:
            return False
        
        # if the item is not in the data set it needs to be added

        # add the val to the data dictionary with the val as the key and the length of the current data list as the value, ( this will represent the index that val will be at in the list self.data )
        self.data_map[val] = len(self.data)

        # add val to the end of the data list
        self.data.append(val)

        return True # return True if val was not already in the data set

    def remove(self, val):

        # if val is not in the data set return False
        if val not in self.data_map:
            return False
        
        # if val is in the data set it needs to be removed from the data set

        last_element_in_list = self.data[-1] # find the value for the last element in the data set
        index_of_element_to_remove = self.data_map[val] # find the index for val in the list ( this will be the index that is removed from the data set )


        # in the dictionary set the value of the last element in the list to the index of the element that is going to be removed
        self.data_map[last_element_in_list] = index_of_element_to_remove
        # set the value at the index of the element that is being removed to the prevoius value of the last index of the list
        self.data[index_of_element_to_remove] = last_element_in_list

        self.data[-1] = val # set the value of the last element in the list to the val ( which is being removed )

        self.data.pop() # pop that value from the list ( remove action )

        self.data_map.pop(val) # pop that value from the dictionary

        return True
    
    def getRandom(self):
        # return a random value from the data set
        return random.choice(self.data)
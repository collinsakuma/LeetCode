class Solution:
    def mergeSimilarItems(self, items1, items2):

        def first_index(item): # call back function to use as key for sorted()
            return item[0] # return the first index of item
        
        all_items = sorted(items1 + items2, key=first_index) # sort a combined list of items1 and 2 using the first index of each item as the key

        merged_items = {} # empty dict to merge items into

        for item in all_items: # loop through all items
            if item[0] not in merged_items: # if item with key item[0] not in dict
                merged_items[item[0]] = item[1] # add item to dict with index 0 as key and index 0 as value
            else:
                merged_items[item[0]] += item[1] # if item already in dict increse the value of that entry by item[1] 
        # problem ask for a list to be returned
        # convert the dict into a list and return list
        return list(merged_items.items()) 
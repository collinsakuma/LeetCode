class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        full_bags = 0 # variable to keep track of bags that are full
        rocks_needed = [0] * len(capacity) # list to be used to quantify bag spare capacity

        for i in range(len(capacity)): 
            rocks_needed[i] = capacity[i] - rocks[i] # for bag i set the rocks_needed[i] to the actual capacity of bag i (capacity - the rocks already inside the bag)

        for bag in sorted(rocks_needed): # sort the rocks_needed bag so that bags that are full and bags that need the least amount of rocks to be filled are looped though first
            if bag == 0: 
                full_bags += 1 # if the bag is already full increment the full_bags count by 1
            elif bag > additionalRocks: # if the bag needs more rocks than are available to be full than the max number of full bags has been found return that number
                return full_bags
            else: # if there is enough rocks to fill the bag
                full_bags += 1 # increment full_bags by 1
                additionalRocks -= bag # reduce the count of additionalRocks by the rocks needed in full bags
        return full_bags
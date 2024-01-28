class Solution:
    def mostFrequent(self, nums, key):
        most_frequent = {} # set an empty dictionary to track number and their frequency behind the key

        for i in range(len(nums) - 1): # loop though range of length numbers minus 1 ( minus 1 because number must come after key )
            if nums[i] == key: # if the number at index i is the key, add the number after it to the dictionary or increment its value if already there
                if nums[i + 1] not in most_frequent: # if number after not in the dict add to the dict with a value of 1
                    most_frequent[nums[i + 1]] = 1
                else: # if the number is already in the dict increment the numbers value by 1
                    most_frequent[nums[i + 1]] += 1

        # sort the dictionaries, key value pairs, sort them by the value, return the key of the last pair in the sorted dict
        return sorted(most_frequent.items(), key=lambda key_val: key_val[1])[-1][0]
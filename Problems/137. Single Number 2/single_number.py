class Solution:
    def singleNumber(self, nums):
        dict = {} # create an empty dictionary

        for num in nums: # loop though numbers in nums create new dict entry if not in dict 
            if num not in dict:
                dict[num] = 1
            else: # if number is already in nums add 1 to that keys value
                dict[num] += 1
        for key in dict: # loop though keys of the dictionary
            if dict[key] == 1: # if the value of the key == 1 return that key
                return key 
        
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hset = {} # set empty dict to keep track of value and at what index

        for index in range(len(nums)): # loop though all elements in the given list
            if nums[index] in hset and abs(index - hset[nums[index]]) <= k:
                # if duplicate is present in the dict at a distance less than or equal to k return True
                return True
            hset[nums[index]] = index # if value not in dict hset create a new entry into the dict

        return False # if no duplicate element is found that meets conditions, return false
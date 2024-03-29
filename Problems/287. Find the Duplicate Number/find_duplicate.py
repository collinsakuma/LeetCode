from collections import Counter

class Solution:
    def findDuplicate(self, nums):
        count = Counter(nums) # use Counter() to create a dict of nums with each number as the key and its frequency in nums as the value
        # Counter.most_common() will order enteriees in the dict in descending order of most frequent keys to least frequent
        # count.most_common()[0] will return the first tuple in the count object
        # count.most_common()[0][0] will return the key in the tuple returned above
        return count.most_common()[0][0]
    
    def findDuplicateTwo(self, nums):
        dictionary = dict() # create a dictionary
        for num in nums: # loop though nums
            if num not in dictionary: # if number not in the dictionary create a new instance with num as the key 
                dictionary[num] = 1
            else: # if the num already in the dictionary the duplicate number has been found return num
                return num
            
    def findDuplicateThree(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
from collections import Counter

class Solution:
    def findDuplicate(self, nums):
        count = Counter(nums) # use Counter() to create a dict of nums with each number as the key and its frequency in nums as the value
        # Counter.most_common() will order enteriees in the dict in descending order of most frequent keys to least frequent
        # count.most_common()[0] will return the first tuple in the count object
        # count.most_common()[0][0] will return the key in the tuple returned above
        return count.most_common()[0][0]

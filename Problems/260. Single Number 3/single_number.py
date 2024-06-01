from collections import Counter

class Solution:
    def singleNumber(self, nums):
        # use Counter() to create a dict of the numbers in nums array and the amount of times the appear
        count = Counter(nums)
        # sort numbers in count dict using their number of occurances as the key
        count = sorted(count.items(), key=lambda x:x[1])

        # return the value of the first two items in the count dict ( first two items are the two who only appear once )
        return [count[0][0], count[1[0]]]
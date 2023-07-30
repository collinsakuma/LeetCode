from collections import Counter

class Solution:
    def findLeastNumberOfUniqueInts(self, arr, k):
        count = Counter(arr) # create a dict using Counter() to make a key value pair of each number in arr as the key and the value as a count of how many times that num is in arr
        ans = len(count) # ans is the length of the count which will have elements removed from it

        for i in sorted(count.values()): # start a loop though the count dict using the values of each key as what is being iterated
            k -= i # since count is being being sorted from smallest to largest minus i from k i representing the count of the number that occurs the least amount of times in arr
            if k < 0: # if k - the number of times i is in arr is < 0 that means more than the allowed elements have been removed exit the loop and return the ans
                break
            ans -= 1 # if k is not 0 decrease ans by 1 as one unique integer has been removed from the list 
        return ans
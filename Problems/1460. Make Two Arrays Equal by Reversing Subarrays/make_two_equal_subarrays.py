from collections import Counter

class Solution:
    def canBeEqual(self, target, arr):
        for num in target: # loop though all numbers in target array
            if num not in arr: # if num not in arr then both arrays cannot become the same
                return False
            if target.count(num) != arr.count(num): # next check if the target array and arr have the same count of num
                return False
        # if all num pass checks arrays can be made equal return True
        return True
    
    def canBeEqualTwo(self, target, arr):
        return Counter(target) == Counter(arr)
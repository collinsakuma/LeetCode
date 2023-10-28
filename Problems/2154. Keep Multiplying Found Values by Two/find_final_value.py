class Solution:
    def findFinalValue(self, nums, original):
        while original in nums: # while original in nums continue the loop
            original = original * 2 # update original price variable by multiplying it by 2
        return original # when original no longer in nums return original 
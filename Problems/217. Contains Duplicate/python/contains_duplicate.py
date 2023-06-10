class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
        # set(nums) will return a list of unique elements from the list
        # compare the length of len(set(nums)) to the length of the original nums list
        # if the length of the two list are not the same that means there is/are duplicates present returning true
            return True
        return False
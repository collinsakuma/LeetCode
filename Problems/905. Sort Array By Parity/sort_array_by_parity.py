class Solution:
    def sortArrayByParity(self, nums):
        n = len(nums) 

        # set arrays for odds numbers, even numbers, and a final array to hold sorted array
        odds = [] 
        evens = []
        final = []

        for i in range(n): # loop though range of len(nums)
            if nums[i] % 2 == 0: # sort nums array into odds and evens if modulo return 0 number is even, append that number to evens array
                evens.append(nums[i])
            else: # odd number append that number to the odds array
                odds.append(nums[i])
        final = final + evens + odds # populate the final array add evens array and then odds array to final
        return final
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
    

    # solution using two pointer method
    def sortArrayByParityTwo(self, nums):
        i, j = 0, len(nums) - 1 # set to pointer to travers list from front and back

        while i < j: # loop while i and j pointers have not converged in the middle
            while i < j and nums[i] % 2 == 0: #if number at index i is an even number increment i
                # ( increment i because even numbers stay at the front of the list )
                i += 1
            while i < j and nums[j] % 2 == 1: # if number at index j is an odd number increment j lower
                # ( increment j because even number go to the end of the list as j is the back half of the list leave the odd number at index j)
                j -= 1
            # if nums[i] is an odd number and nums[j] is an even number swap the two vales so the even number 
            nums[i], nums[j] = nums[j], nums[i]
        
        return nums
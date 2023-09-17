class Solution:
    def sumOfMultiples(self, n):
        total_sum = 0

        for i in range(1, n + 1): # loop though range of 1 to (n + 1)
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0: # check each number if the mod of 3,5, or 7 == 0
                # if any condition met add number to total_sum
                total_sum += 1
        return total_sum # return total_sum
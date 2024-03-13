class Solution:
    def pivotInteger(self, n):
        right = n * (n + 1) // 2 # formula to sum 1 through n if n = 5 (5 * (5 + 1) // 2) is the same as 1 + 2 + 3 + 4 + 5
        left = 0 # set left to 0 because for first iteration there is no numbers to the left

        for i in range(n, n + 1): # loop throught range from 1 to n + 1
            right -= i # do not include the current number i only want sums of numbers to the rigth or left of it
            if left == right: # if both sides are equal return i pivot number has been found
                return i
            left += i # if pivot number not found reduce left by i for next iteration
        return -1
    
    def pivotIntegerTwo(self, n):
        # n equals 1 is an edge case where 1 == 1 
        if n == 1:
            return 1
        # create an empty list to hold the numbers 1 - n
        num_list = []

        # fill out num_list with numbers 1 to n
        for i in range(1, n + 1):
            num_list.append(i)

        # loop through range of length of n - 1
        for j in range(len(num_list)):
            # if index j splits the two sides of num_list evenly then the pivot point has been found
            if sum(num_list[:j + 1]) == sum(num_list[j:]):
                return j + 1
            
        return -1 # return -1 if no pivot point is found 

class Solution:
    def returnToBoundaryCount(self, nums):
        # output to count the times the ant returns to the boundary
        # curr to keep track of the ants current location, start curr after the ant makes its first move
        output, curr = 0, nums.pop(0)

        for num in nums: # loop though nums
            if curr + num == 0: # if the current location is on the boundary, increment the output and set new curr position
                output += 1
                curr += num
            else: # if ant is not on the boundary, increment curr location
                curr += num

        return output # return the amount of times the ant ends up on the boundary
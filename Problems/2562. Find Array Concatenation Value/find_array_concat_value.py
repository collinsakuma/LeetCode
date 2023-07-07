class Solution:
    def findTheArrayConcVal(self, nums):
        output = 0 # set a variable for the output

        if len(nums) % 2 == 1: # check if the length of nums is an uneven number
            output = nums[len(nums) // 2] # if len nums is odd set output equal to the middle index
        for i in range(len(nums) // 2): # loop thought range of len nums divided by 2, only need to loop though half or range because you add first and last at same time
            output += int(str(nums[i]) + str(nums[len(nums) - 1 - i])) # concatenate the current index and the last index that havent been added to the output. then add the concatenated value as a int
        return output
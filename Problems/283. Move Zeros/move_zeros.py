class Solution:
    def moveZeros(self, nums):
        count = 0 # count variable it set to keep track of how many numbers have been looped over
        curr = 0 # curr is to keep track of current index, if a zero is found the curr index stays the same because it is removed and appended to the back of nums

        while count != len(nums): # loop though range of len(nums) keep track of by count
            if nums[curr] == 0: # if the number at the current index is 0
                nums.appned(nums.pop(curr)) # pop the 0 at that index and append it to the back of the nums array
                count += 1 # increment count by 1 only because there is a new number at index curr
            else: # if number is not 0 increment both count and curr by 1
                curr += 1
                count += 1
        
        # modifying nums in place so no need to return anything
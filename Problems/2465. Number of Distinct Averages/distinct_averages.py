class Solution:
    def distinctAverages(self, nums):
        averages = [] # empty list to add unique averages too
        nums = sorted(nums) # sort nums from least to greatest

        while len(nums) >= 2: # while nums has 2 or more numbers in it continue the loop
            # find the avearge between the smallest and largest number in nums list
            curr_average = (nums.pop(0) + nums.pop(-1)) / 2
            if curr_average not in averages: # check if th curr_average is in averages
                # if not in averages append to the list
                averages.append(curr_average)
        
        return len(averages) # return the count of unique averages
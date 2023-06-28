class Solution:
    def minMaxGame(self, nums):

        new_nums = nums # create copy of nums

        while len(new_nums) != 1: # start a loop untill the length of the list is 1
            is_min = True # set to true and use to switch between min and max
            new_new_nums = [] # for each consecutive loop reset new_new_nums to an empty list

            for i in range(0, len(new_nums), 2): # loop though the range of new_nums length by increment by 2
                if is_min: # if is_min is true
                    new_new_nums.append(min(new_nums[i], new_nums[i + 1])) # append the min value of both indecies
                else: # if is_min is not true
                    new_new_nums.append(max(new_nums[i], new_nums[i + 1])) # append the max value of both indecies
                is_min = not is_min # for each loop set is_min to the oposite
            new_nums = new_new_nums # set new_nums equal to the new list to start the loop over again if its legnth is greater than 1
        return new_nums[0] # return the first index ( should be only index left )
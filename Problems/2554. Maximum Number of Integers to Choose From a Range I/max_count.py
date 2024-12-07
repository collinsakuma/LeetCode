class Solution:
    def maxCount(self, banned, n, maxSum):
        num_chosen = 0 # number of nums used
        curr_sum = 0 # current sum of numbers chosen

        # loop through range of 1 to n
        for i in range(1, n + 1):
            if i not in banned:
                # if number is not banned check if it can be added to the
                # current sum without exceeding the max sum
                if curr_sum + i > maxSum:
                    # if curr sum will be greater than max sum return the 
                    # current number of chosen numbers
                    return num_chosen
                else:
                    # add to current sum, increase the number of chosen numbers
                    curr_sum += i
                    num_chosen += 1
        
        return num_chosen
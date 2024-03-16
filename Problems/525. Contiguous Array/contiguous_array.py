from collections import defaultdict

class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        # initalize dict with key of prefix sum and value of left most index who has that prefix sum
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0] = -1

        max_length = 0

        for index, number in enumerate(nums):
            # add 1 for one and minus 1 for zero
            if number:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # check if the subarray has an equal number of 0s and 1s
            # update max length
            if prefix_sum in prefix_sum_dict:
                max_length = max(max_length, (index - prefix_sum_dict[prefix_sum]))
            else:
                # update left most index for specified index sum
                prefix_sum_dict[prefix_sum] = index
        
        return max_length

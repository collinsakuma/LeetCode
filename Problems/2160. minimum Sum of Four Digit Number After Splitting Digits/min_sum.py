class Solution:
    def minimumSum(self, num):
        sorted_num = sorted(str(num)) # turn num into a sorted string from smallest number to largest
        # create two number pairs with the two smallest numbers at the 10th spot for each number, add numbers together to get th minimum sum
        return int(sorted_num[0] + sorted_num[2]) + int(sorted_num[1] + sorted_num[3])
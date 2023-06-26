class Solution:
    def maxProductDifference(self, nums):
        sorted_nums = sorted(nums)
        
        return (sorted_nums[-1] * sorted_nums[-2]) - (sorted_nums[0] * sorted_nums[1])
        # want the difference between the product of the two largest numbers and two smallest numbers
        # 1. sort the array using sorted()
        # 2. (a, b) use the two numbers at the end of the sorted array index -1, -2
        # 3. (c, d) use the two smallest numbers at the begining of the array 0, 1
        # 4. return the largest difference possible. 
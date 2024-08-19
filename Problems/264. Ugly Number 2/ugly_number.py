class Solution:
    def nthUglyNumber(self, n):
        ugly_nums = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly_nums) < n:
            next_ugly = min(ugly_nums[i2] * 2, ugly_nums[i3] * 3, ugly_nums[i5] * 5)
            ugly_nums.append(next_ugly)

            if next_ugly == ugly_nums[i2] * 2:
                i2 += 1
            if next_ugly == ugly_nums[i3] * 3:
                i3 += 1
            if next_ugly == ugly_nums[i5] * 5:
                i5 += 1
        
        return ugly_nums[-1]
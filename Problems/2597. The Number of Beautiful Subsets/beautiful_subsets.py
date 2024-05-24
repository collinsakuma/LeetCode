class Solution:
    def beautifulSubsets(self, nums, k):
        def is_safe(nums, part, j, k):
            for n in part:
                if abs(nums[j] - n) == k:
                    return False
            return True

        self.count = 0
        part = []

        def subset_arr(i):
            if i >= len(nums):
                self.count = self.count + 1
                return 

            if is_safe(nums, part, i, k):
                part.append(nums[i])
                subset_arr(i + 1)
                part.pop()
            subset_arr(i + 1)

        subset_arr(0)

        return self.count - 1
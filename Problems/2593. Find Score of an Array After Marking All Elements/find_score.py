class Solution:
    def findScore(self, nums):
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        score = 0

        for num, idx in sorted_nums:
            # if number has not been marked add to score
            if nums[idx] != -1:
                score += num
                nums[idx] = -1 # mark current index as seen
                if idx > 0:
                    nums[idx - 1] = -1 # mark left neighbor
                if idx < n - 1:
                    nums[idx + 1] = -1 # mark right neighbor

        return score # return score
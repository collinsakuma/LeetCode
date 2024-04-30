class Solution:
    def minOperations(self, nums, k):
        final_xor = 0
        count = 0

        for n in nums:
            final_xor = final_xor ^ n

        while k or final_xor:
            if (k % 2) != (final_xor % 2):
                count += 1

            k //= 2
            final_xor //= 2

        return count
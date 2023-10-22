class Solution:
    def minNumber(self, nums1, nums2):
        common, m1, m2 = set(nums1).intersection(nums2), min(nums1), min(nums2)
        return min(common) if common else min(m1, m2) * 10 + max(m1, m2)
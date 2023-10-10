class Solution:
    def merge(self, nums1, m, nums2, n):
        # i equals the last number in the nums1 array
        # j equals the last number in the nums2 array
        # index represents the last possible index that a number should be at
        i, j, index = m - 1, n - 1, m + n - 1
        
        while j >= 0: # while there are still numbers to loop though in j
            # if there are still numbers in i to loop through and nums1 at given index i is greater than num2 at given index j
            if i >= 0 and nums1[i] > nums2[j]:
                # set the value of nums1 at index to nums1[i]
                nums1[index] = nums1[i]
                i -= 1 # decrease i by 1
            else: # if num2 at index j is greater set index value to nums2[j]
                nums1[index] = nums2[j]
                j -= 1 # decrease j by 1
            index -= 1 
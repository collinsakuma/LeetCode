class Solution:
    def getCommon(self, nums1, nums2):
        left, right = 0, 0 # set up two pointers

        # start a loop that while continue as long as the left and right pointers havent reached the end of their lists
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]: # if the two values at indexes left and right are equal return the value
                return nums1[left]
            else:
                # increment the side thats value is lower
                if nums1[left] > nums2[right]: # if left is greater than right
                    right += 1 # increment right
                else:
                    left += 1 # if right is greater than left increment

        return -1 # if no matching numbers are found return -1
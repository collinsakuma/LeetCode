class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2) # combine the two arrays and sort the new array
        if len(nums) % 2 != 0: # if the length of the array is an odd amount
            return nums[len(nums) // 2] # return the middle number of the array
        else: # if the length of the array is an even number add the two middle numbers and divide the sum by 2
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
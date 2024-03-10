class Solution:
    def intersection(self, nums1, nums2):
        output = [] # array to hold the intersections of the two arrays

        for num in set(nums1): # looop though a set of nums1
            # if num is an intersection of both arrays
            if num in nums2:
                # add that number to the output array
                output.append(num)
        
        return output # return intersections
from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        output = [] # list of intersecting numbers

        # function to build out intersecting numbers list
        def intersection_loop(list_1, list_2):
            # loop through list_1
            for num in list_1:
                # if num in list_2 add the number to the interesection array and remove that number from list_2
                if num in list_2:
                    output.append(num)
                    list_2.remove(num)

        # traverse the shorter of the two list 
        if len(nums1) < len(nums2):
            intersection_loop(nums1, nums2)
        else:
            intersection_loop(nums2, nums1)

        return output
    
    # optimized runtime answer using Counter() method
    def intersectTwo(self, nums1, nums2):
        count_nums1 = Counter(nums1)
        count_nums2 = Counter(nums2)
        # & operator is used to take the intersections of two python sets
        intersecting = count_nums1 & count_nums2

        return list(intersecting.elements())

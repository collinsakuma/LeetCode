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
    

    def intersectThree(self, nums1, nums2):
        # create dicts for the two list with each number and their count in the list
        count_1 = Counter(nums1)
        count_2 = Counter(nums2)

        # initalize an empty array to hold the intersecting numbers
        intersecting = []

        # loop though number in count_1
        for num in count_1.keys():
            # if that number is also in the other list
            if num in count_2:
                # add the number to the, as many times as the minimium occurance in either list
                intersecting.extend(num * min(count_1[num], count_2[num]))

        return intersecting 
class Solution:
    def findDifference(self, nums1, nums2):
        answer = [[], []]
        for i in set(nums1): # loop through set of nums1
            if i not in set(nums2): # if number not in a set of nums2 then append it to the first list of answer
                answer[0].append(i)
        for j in set(nums2): # loop though set of nums2
            if j not in set(nums1): # if number not in a set of nums1 append the number to the second list of answer
                answer[0].append(j)
        return answer # return the two list
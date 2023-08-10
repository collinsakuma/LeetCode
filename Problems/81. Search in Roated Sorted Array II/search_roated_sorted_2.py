class Solution:
    def search(self, nums, target):
        # set two pointer variables
        begin = 0 
        end = len(nums) - 1

        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]: # the side that is sorted is unknown
                end -= 1
            elif nums[mid] > nums[end]: # if the number in at mid is greater than nums[end] that means numbers on the left of that are sorted
                if nums[begin] <= target and target < nums[mid]: # if target is between nums[begin] and nums[mid] target will be on the left side
                    end = mid - 1
                else: # in the right side
                    begin = mid + 1
            else: # the rigth side is sorted
                if nums[mid] < target and target<= nums[end]: # target is on the right side
                    begin = mid + 1
                else: # target on left
                    end = mid - 1
        return False
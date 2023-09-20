class Solution:
    def validMountainArray(self, arr):
        # if the length is less than three then it cannot be a valid mountain array
        if len(arr) < 3:
            return False

        # set two pointer variables
        left, right = 0, len(arr) - 1

        # 1st check if left variable is less than length of the list
        # 2nd check if element at arr[left] is less than element to its right
        while left + 1 < len(arr) - 1 and arr[left] < arr[left + 1]:
            left += 1 # while both condition are true increment left
        
        # 1st check right is greater than 0, (right starts at end of list and increments down)
        # 2nd check that element at arr[right] is less than element to its left
        while right - 1 > 0 and arr[right] < arr[right - 1]:
            right -= 1 # while both conditions are still true decrease right by 1

        # if left and rigth are equal then the increasing and decreasing have meet on the same number meaning it is a valid mountain array
        return left == right
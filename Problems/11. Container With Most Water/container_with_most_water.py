class Solution:
    def maxArea(self, height):
        # set left and right variables and area
        left, right, area = 0, len(height) - 1, 0
        while left < right:
            # compare the current area with area of the width * the minimum height of right or left
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: # increment based on which height is taller
                left += 1
            else: # if left side is higher increment the right side
                right -= 1

        return area
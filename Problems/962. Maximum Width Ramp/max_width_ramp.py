class Solution:
    def maxWidthRamp(self, nums):
        max_width = 0 # track max width

        # loop through range of numbers
        for i in range(len(nums)):
            # loop through the range of numbers left after i in reverse order
            for j in range(len(nums) - 1, i, -1):
                # if nums[i] <= nums[j] check for a new max width
                if nums[i] <= nums[j]:
                    # check for new max width
                    max_width = max(max_width, j - i)
                # if remaning widths are no wider than the current max, break from the loop ( do not check rest )
                if j - i < max_width:
                    break
        
        return max_width # return the max width
    
    def maxWidthRampTwo(self, nums):
        # initialize a stack and save the length of nums as a variable
        n = len(nums)
        stack = []

        # loop through range
        for i in range(n):
            # if no nums in stack or if last number in the stack is greater than nums[i]
            if not stack or nums[stack[-1]] > nums[i]:
                # add the number to the stack
                stack.append(i)

        # set answer
        ans = 0

        # loop through range backwards
        for i in range(n - 1, 0, -1):
            # while stack and condition still met
            while stack and nums[stack[-1]] <= nums[i]:
                # check for a new widest ramp
                ans = max(ans, i - stack[-1])
                # pop from the stack
                stack.pop()

        return ans
